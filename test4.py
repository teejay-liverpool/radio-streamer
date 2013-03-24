import smbus
import sys
import getopt
import time
bus = smbus.SMBus(1)


delay = 0.3
bus.write_byte_data(0x20,0x00,0xff) # Port A with A0-A6 outputs A7 input

bus.write_byte_data(0x20,0x0C,0xff)

while 1: 
	a = bus.read_byte_data(0x20,0x12)
	#a = a  >> 7
	print a
	time.sleep(delay)

