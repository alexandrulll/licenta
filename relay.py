import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.OUT)
GPIO.output(32, GPIO.HIGH)

try:
	GPIO.output(32, GPIO.LOW)
	print('Relay 1 is ON')
	time.sleep(2)
	GPIO.cleanup()
	print('Relay 1 is OFF!!!')
	
except KeyboardInterrupt:
		print('QUIT')
		GPIO.cleanup()