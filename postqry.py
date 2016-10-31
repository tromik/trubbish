import psycopg2

conn = psycopg2.connect(database="datamart", user="datamart", password="pervasive", host="TORFIN04", port="5432")

print "Opened database successfully"
