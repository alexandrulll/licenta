import psycopg2

conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

create_table_query = """CREATE TABLE dht11(
    id integer PRIMARY KEY,
    temperature text,
    humidity text);"""

cur.execute(create_table_query)
	
 connection.commit()
 
 print("Table created successfully in PostgreSQL ")