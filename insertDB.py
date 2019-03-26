import psycopg2
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

pin = 23
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

cur.execute("INSERT INTO users dht11 (%s, %s, %s)", (10, '25', '89'))

while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:	
		cur.execute("INSERT INTO dht11 (%s, %s, %s)", (1, 'temperature', 'humidity'))
		conn.commit()
	else:
		print('Failed to get reading. Try again!')
	time.sleep(.500)