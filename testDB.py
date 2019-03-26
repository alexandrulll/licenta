import psycopg2

conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

cur.execute("""CREATE TABLE dht11(
    id integer PRIMARY KEY,
    temperature text,
    humidity text""")conn.commit()

results = cur.fetchall()

for result in results:
    print(result)
