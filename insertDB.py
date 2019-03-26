import psycopg2
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

pin = 23
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:	
		cur.execute("INSERT INTO dht11 VALUES (%s, %s, %s)", (10, temperature, humidity))
		conn.commit()
	else:
		print('Failed to get reading. Try again!')
	time.sleep(.500)