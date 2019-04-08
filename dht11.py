import Adafruit_DHT
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.HIGH)

sensor = Adafruit_DHT.DHT11

pin = 23
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		GPIO.output(38, GPIO.LOW)
		print('Relay 1 is ON')
		print temperature, humidity
	else:
		print('Failed to get reading. Try again!')
	time.sleep(.500)