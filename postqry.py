import psycopg2
import psycopg2.extras
import datetime

# Try to connect
try:
    conn = psycopg2.connect(database="datamart", user="datamart", password="pervasive", host="TORFIN04", port="5432")
except:
    print "I am unable to connect to the database."

# If we are accessing the rows via column name instead of position we
# need to add the arguments to conn.cursor.
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    cur.execute("""
select
cast('Hotel' as varchar(50)) as type,
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
AND b."Date_of_First_Travel" = current_date - interval '2 days'
AND coalesce(s."EntityID") = 2
Order By type, service_id, gl_account_name""")
except:
    print "I can't SELECT --> Prepost Cost Accrual Query"


# Note that below we are accessing the row via the column name.
rows = cur.fetchall()
for row in rows:
    debit_amount = 0.00
    credit_amount = 0.00
    if row['gl_account_name'] == "Accrued Liabilities":
        credit_amount = row['amount']
        case = 'credit'
    else:
        debit_amount = row['amount']
        case = 'debit'

    gl_reference = str(row['booking_no']) + "-" + str(row['paid_by'])
    dist_reference = str(row['service_id']) + "-" + str(row['service_start_date'])

    modified_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print str(row['service_id']) + " | " + str(row['gl_account_name']) + " | " + str(debit_amount) + " | " + str(credit_amount) + " | " + str(modified_date) + " | " + case + " | " + str(row['type'])

    

conn.close()
