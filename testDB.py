import psycopg2

conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

create_table_query = """CREATE TABLE dht11(
    id SERIAL PRIMARY KEY,
    temperature numeric,
    humidity numeric);"""

cur.execute(create_table_query)
conn.commit()
print("Table created successfully in PostgreSQL ")