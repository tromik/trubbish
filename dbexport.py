import csv
import psycopg2
import psycopg2.extras
from datetime import datetime, timedelta


env = 'prod'

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
except psycopg2.OperationalError as e:
    print('Unable to connect! Host: ' + host_name + '  Database: ' + database_name +'\n{0}').format(e)

# Open cursor with field names
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

datadate = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

sql_table = 'trip_cost_accruals_entity'

file_name = 'gafrica_trip_cost_accruals_' + str(datadate) + '.csv'

# Get open trip cost accruals
sel_query = """select
                *
                from """ + sql_table + """
                where reversed_date is NULL
                and gl_account_name !~* 'Liabilities'"""

try:
    cur.execute(sel_query)
except psycopg2.OperationalError as e:
    print('Unable to execute select statement!\n{0}').format(e)

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\n',
    quoting = csv.QUOTE_MINIMAL)

rows = cur.fetchall()

headers = [desc[0] for desc in cur.description]

with open(file_name, 'w') as csvfile:
    datawriter = csv.writer(csvfile, dialect='mydialect')

    datawriter.writerow(headers)

    for row in rows:
        datawriter.writerow(row)

cur.close()
conn.close()
