import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.OUT)
GPIO.output(32, GPIO.HIGH)

GPIO.setup(36, GPIO.OUT)
GPIO.output(36, GPIO.HIGH)

try:
	GPIO.output(32, GPIO.LOW)
	print('Relay 1 is ON')
	time.sleep(2)
	GPIO.output(36, GPIO.LOW)
	print('Relay 2 is ON')
	time.sleep(4)
	GPIO.cleanup()
	print('Relay 1 and 2 are OFF!!!')
	
except KeyboardInterrupt:
		print('QUIT')
		GPIO.cleanup()