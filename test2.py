import smbus
import time
 
bus = smbus.SMBus(1)

v = bus.read_byte_data(0x20,0x58)

print v
 
#for a in range(0,256):
#	bus.write_byte(0x20,a)
#	time.sleep(0.1)

