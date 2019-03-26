import psycopg2

conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

cur.execute("DROP TABLE dht11;")
conn.commit()
print("Table droped successfully in PostgreSQL ")