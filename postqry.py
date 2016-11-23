import psycopg2
import psycopg2.extras
import datetime

env = 'dev'

if env == 'prod':
    database_name = 'xyz'
    user_name = 'xyz'
    pass_word = 'xyz'
    host_name = 'xyz'
    port_num = '5432'
else:
    database_name = 'xyz'
    user_name = 'xyz'
    pass_word = 'xyz'
    host_name = 'xyz'
    port_num = '5432'

# Connect to the database
try:
    conn = psycopg2.connect(database=database_name, user=user_name, password=pass_word, host=host_name, port=port_num)
    print 'Connection successful...'
except psycopg2.OperationalError as e:
    print('Unable to connect!\n{0}').format(e)
    print "I am unable to connect to the database. Host: " + host_name + "  Database: " + database_name
    sys.exit(1)

# Open cursor with field names
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

booking_doft_qry = '2016-11-21'

sel_query = """select cast('Hotel' as varchar(50)) as type,
                s."ServiceID" as service_id,
                s."BookingNo" as booking_no,
                b."Date_of_First_Travel" as date_of_first_travel,
                s."Service_Start_Date" as service_start_date,
                cast(s."Vendor_Code" as varchar(35)) as vendor_code,
                cast(case when (s."Cost_Currency" = 'ZAR') then 'ZAR' else 'USD' end as varchar(5)) as currency,
                s."Paid_By" as paid_by,
                case when (s."Cost_Currency" = 'ZAR') then s."Validated_Cost_Local" else s."Validated_Cost_USD" end as amount,
                s."EntityID" as entity_id,
                m.markup,
                gl.gl_account_name,
                gl.gl_account_number,
                gl.company,
                cast(gl.revenue_stream as varchar(100)) as revenue_stream
                from service s
                Left Join booking b ON s."BookingNo" = b."BookingNo"
                Left Join smart_project_entity e
                on coalesce(s."EntityID", 1) = e.id
                Left Join smart_project_servicetypemarkup m
                on e.id = m.entity_id
                and m.service_type = 'Pre Hotel'
                Join tour_cost_gl_mappings_africa gl
                on gl.revenue_stream = 'Accomodation'
                and (gl.gl_account_name = 'Accommodation'
                or gl.gl_account_name = 'Accrued Liabilities')
                Where s."Service_Type" = 'Hotel'
                AND s."Service_Status" = 'Confirmed'
                AND s."Paid_By" IN ('D-LO','Ldr','D-TO')
                AND (s."Expected_Cost_Currency" is not null OR s."Validated_Cost_Currency" is not null)
                AND (s."Expected_Cost_Local" > 0 OR s."Validated_Cost_Local" > 0)
                AND char_length(s."Invoice_Number") = 0
                AND b."Date_of_First_Travel" = current_date - interval '2 days'
                AND coalesce(s."EntityID") = 2

                UNION ALL

                select
                cast('Transfer' as varchar(50)) as type,
                s."ServiceID" as service_id,
                s."BookingNo" as booking_no,
                b."Date_of_First_Travel" as date_of_first_travel,
                s."Service_Start_Date" as service_start_date,
                cast(s."Vendor_Code" as varchar(35)) as vendor_code,
                cast(case when (s."Cost_Currency" = 'ZAR') then 'ZAR' else 'USD' end as varchar(5)) as currency,
                s."Paid_By" as paid_by,
                case when (s."Cost_Currency" = 'ZAR') then s."Validated_Cost_Local" else s."Validated_Cost_USD" end as amount,
                s."EntityID" as entity_id,
                m.markup,
                gl.gl_account_name,
                gl.gl_account_number,
                gl.company,
                cast(gl.revenue_stream as varchar(100)) as revenue_stream
                from service s
                Left Join booking b ON s."BookingNo" = b."BookingNo"
                Left Join smart_project_entity e
                on coalesce(s."EntityID", 1) = e.id
                Left Join smart_project_servicetypemarkup m
                on e.id = m.entity_id
                and m.service_type = 'Pre Hotel'
                Join tour_cost_gl_mappings_africa gl
                on gl.revenue_stream = 'Transfer'
                and (gl.gl_account_name = 'Transfer'
                or gl.gl_account_name = 'Accrued Liabilities')
                Where s."Service_Type" = 'Transfer'
                AND s."Service_Status" = 'Confirmed'
                AND s."Paid_By" IN ('D-LO','Ldr','D-TO')
                AND (s."Expected_Cost_Currency" is not null OR s."Validated_Cost_Currency" is not null)
                AND (s."Expected_Cost_Local" > 0 OR s."Validated_Cost_Local" > 0)
                AND char_length(s."Invoice_Number") = 0
                --AND b."Date_of_First_Travel" = current_date - interval '2 days'
                AND b."Date_of_First_Travel" = '""" + booking_doft_qry + """'
                AND coalesce(s."EntityID") = 2
                Order By type, service_id, gl_account_name"""

try:
    cur.execute(sel_query)
except psycopg2.OperationalError as e:
    print "Unable to SELECT --> Prepost Cost Accrual Query"
    print('Unable to execute select statement!\n{0}').format(e)
    sys.exit(1)

# Keep a count of all inserts
ins_count = 0

rows = cur.fetchall()
for row in rows:

    # Row-by-row processing occurrs here

    debit_amount = 0.00
    credit_amount = 0.00

    # Set debit and credit values, always credit Accrued Liabilities account
    if row['gl_account_name'] == "Accrued Liabilities":
        credit_amount = row['amount']
        case = 'credit'
    else:
        debit_amount = row['amount']
        case = 'debit'

    # gl_reference is format booking_no-paid_by
    gl_reference = str(row['booking_no']) + "-" + str(row['paid_by'])

    # dist_reference is format service_id-service_start_date
    dist_reference = str(row['service_id']) + "-" + str(row['service_start_date'])

    # Data to be inserted
    ins_data = (str(row['booking_no']), str(row['service_id']), str(row['date_of_first_travel']), str(row['service_start_date']),
                str(row['vendor_code']), str(row['paid_by']), str(row['type']), str(row['gl_account_name']), str(row['gl_account_number']),
                str(row['currency']), str(row['amount']), str(row['type']), gl_reference, dist_reference,
                '{0:.2f}'.format(debit_amount), '{0:.2f}'.format(credit_amount), str(row['entity_id']), str(row['company']), str(row['type']))

    # Insert statement
    ins_stmt = '''insert into prepost_cost_accruals_entity 	(booking_no, service_id, date_of_first_travel, service_start_date,
				                                            vendor_code, paid_by, service_type, gl_account_name, gl_account_number,
                                            				currency, amount, stage, gl_reference, dist_reference,
                                            				debit_amount, credit_amount, entity_id, company, revenue_stream,
                                            				created_date, modified_date)
                                                            values(%s, %s, %s, %s,
                                                                    %s, %s, %s, %s, %s,
                                                                    %s, %s, %s, %s, %s,
                                                                    %s, %s, %s, %s, %s,
                                                                    now(), now());'''

    try:
        cur.execute(ins_stmt, ins_data)
        print 'Inserting...'
        ins_count = ins_count + 1
    except psycopg2.OperationalError as e:
        print 'Cannot insert into database ' + str(database_name) + ' on servier ' + str(host_name)
        print('Unable to insert!\n{0}').format(e)
        sys.exit(1)


try:
    conn.commit()
    print 'Committing...' + str(ins_count) + ' rows inserted.'
except psycopg2.OperationalError as e:
    print 'Cannot commit insert statement'
    print('Unable to commit!\n{0}').format(e)

cur.close()
print 'Cursor closed'
conn.close()
print 'Connection closed'
