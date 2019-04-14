import serial

ser = serial.Serial('/dev/ttyACM0',9600)
i = 0
while (i < 1):
	read_serial=ser.readline()
	print read_serial
	i += 1
