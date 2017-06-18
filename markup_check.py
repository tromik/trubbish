# Import smtplib for the actual sending function
import smtplib
import psycopg2

polaris_server = '172.16.10.54'
polaris_database = 'polaris'
polaris_user = 'datamart'
polaris_password = 'pervasive'

try:
    conn = psycopg2.connect("dbname=polaris_database user=polaris_user host=polaris_server password=polaris_password")
except:
    print("Error connecting to database %s on server %s!" % (polaris_database, polaris_server))

# Import the email modules we'll need
from email.mime.text import MIMEText
msg = MIMEText('This is a test e-mail.\n\nCheers,\nTom')

sql_load = """select * from
(
select distinct t.id as trip_id, t.dossier_code, t.trip_name from departures d join trips t on d.trip_id = t.id where d.cancelled = 'f' and d.suppressed = 'f' and d.start_date >= '2016-08-01' and entity_id = 2 and d.polaris_only = 'f'
union
select distinct t.id as trip_id, t.dossier_code, t.trip_name from services_hotels s join departures d on s.departure_id = d.id join trips t on d.trip_id = t.id where s.deleted = 'f' and s.cancelled = 'f' and service_date >= '2016-08-01' and d.entity_id = 2 and d.polaris_only = 'f'
union
select distinct t.id as trip_id, t.dossier_code, t.trip_name from services_transfers s join departures d on s.departure_id = d.id join trips t on d.trip_id = t.id where s.deleted = 'f' and s.cancelled = 'f' and service_date >= '2016-08-01' and d.entity_id = 2 and d.polaris_only = 'f'
) x
where x.trip_id not in
(select distinct trip_id from smart_project_servicetypemarkup where trip_id is not NULL);"""

cur = conn.cursor()
try:
    cur.execute(sql_load)
except:
    print("Error executing select statement against database %s on server %s!" % (polaris_database, polaris_server))

rows = cur.fetchall()
for row in rows:
    print("   ", row[1][1])

msg['Subject'] = 'TEST TEST' # 'The contents of %s' % textfile
msg['From'] = 'integration@gadventures.com'
msg['To'] = 'tomr@gadventures.com'


# Send the message via our own SMTP server.
s = smtplib.SMTP('tordcrelay01.gadventures.internal')
s.send_message(msg)
s.quit()
