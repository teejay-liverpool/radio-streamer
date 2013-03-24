
import sys
import getopt
import time
import os
from subprocess import Popen

def checkUSBExists():
   if os.path.ismount("/mnt/usb"):
	print "mounted"
   else:
	print "not"

def getWifi():
   f = open("/mnt/usb/wifi.txt", 'r')

   global router 
   router = str(f.readline() )
   router = router[ router.index("=") +1 : ]
   router = router.rstrip('\r\n')
   print router

   global password 
   password = str(f.readline() )
   password = password[ password.index("=") +1 : ]
   password = password.rstrip('\r\n')
   print password

   f.close()

def createConfigFile():
	if os.path.exists("/etc/network/interfaces"):
		os.remove("/etc/network/interfaces")
	
	file = open("/etc/network/interfaces", 'w')
	
	file.write("auto lo \n")
	file.write("\n")
	file.write("iface lo inet loopback \n")
	file.write("iface eth0 inet dhcp \n")
	file.write("\n")
	file.write("allow-hotplug wlan0 \n")
	file.write("iface wlan0 inet dhcp \n")
	file.write("wpa-ssid \"" + router + "\" \n" )
	file.write("wpa-psk \"" + password + "\" \n" )
	file.close()

checkUSBExists()

getWifi()

createConfigFile()


