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
    database_name = 'datamart'
    user_name = 'datamart'
    pass_word = 'pervasive'
    host_name = 'TORFIN04'
    port_num = '5432'

# Connect to the database
try:
    conn = psycopg2.connect(database=database_name, user=user_name, password=pass_word, host=host_name, port=port_num)
    print 'Connection successful...'
except psycopg2.OperationalError as e:
    print('Unable to connect!\n{0}').format(e)
    print "I am unable to connect to the database. Host: " + host_name + "  Database: " + database_name
    sys.exit(1)

trip_code = 'GAPCCCR170402-O1'

def sql_select(trip_code):

    # Open cursor with field names
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    sel_query = """SELECT
                        "Service_Status" 		AS service_status,
                        "Reporting_office" 		AS reporting_office,
                        "Dossier_Code" 			AS dossier_code,
                        "Parent_Trip_Code" 		AS parent_trip_code,
                        "Child_Trip_Code" 		AS child_trip_code,
                        main_date,
                        daystostartdate 		AS days_to_start_date,
                        start_date,
                        "TripId" 			    AS trip_id,
                        "ServiceID" 			AS service_id,
                        "BookingNo" 			AS booking_no,
                        "No_Of_PAX" 			AS num_pax,
                        "Base_Price_USD" 		AS base_price_usd,
                        "Discount_Amount_USD" 	AS discount_amount_usd,
                        "Actual_Price_USD" 		AS actual_price_usd,
                        "Agent_Commission_USD" 	AS agent_commission_usd,
                        netrevenue 			    AS net_revenue,
                        "Expected_Cost_USD" 	AS expected_cost_usd,
                        "Validated_Cost_USD" 	AS validated_cost_usd,
                        netmargin 			    AS net_margin,
                        control,
                        "Trip_Name" 			AS trip_name,
                        source
                    FROM dmv_gtd_final_qry_with_booking_lumos gtd;"""

    try:
        cur.execute(sel_query)
    except psycopg2.OperationalError as e:
        print "Unable to SELECT --> gtd"
        print('Unable to execute select statement!\n{0}').format(e)
        sys.exit(1)

    rows = cur.fetchall()
    for row in rows:

        # Row-by-row processing occurrs here
        if (row['child_trip_code'] == trip_code):
            print 'trip code: ' + row['child_trip_code'] + ' | expected_cost_usd: ' + str(row['expected_cost_usd']) + ' | validated_cost_usd: ' + str(row['validated_cost_usd'])

    cur.close()
    print 'Cursor closed'

sql_select(trip_code)

conn.close()
print 'Connection closed'
