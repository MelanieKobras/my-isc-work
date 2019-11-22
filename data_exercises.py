from datetime import datetime
import serial
import io

ser= serial.Serial(port='/dev/ttyUSB0',baudrate=9600)
print(ser.read(size=8))

ser = serial.Serial( port='/dev/ttyUSB0', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

