import smbus
import sys
import getopt
import time
bus = smbus.SMBus(1)

delay = 0.3

bus.write_byte_data(0x20,0x00,0xff) # input
bus.write_byte_data(0x20,0x01,0xff) # input


while 1: 
	a = bus.read_byte_data(0x20,0x12)
	print "a = " + str(a)
	time.sleep(delay)

#	b = bus.read_byte_data(0x20,0x13)
#	print "b = " + str(b)
#	time.sleep(delay)

