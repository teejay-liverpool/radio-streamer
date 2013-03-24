import smbus
import sys
import getopt
import time
import os
from subprocess import Popen

currentStation = 0

volumeLevel = 90
volStep = 10

nextStationButton = 127
upVolumeButton    = 254
downVolumeButton  = 223

def setVolume( volLevel ): 
	os.system("amixer cset numid=1 -- " + str(volLevel) + "%")

def upVolume():
	global volumeLevel
        volumeLevel += volStep

	if volumeLevel > 100:
		volumeLevel = 100
	setVolume( volumeLevel )
def downVolume():
	global volumeLevel
	volumeLevel -= volStep
	if volumeLevel < 0:
		volumeLevel = 0
	setVolume( volumeLevel )

def nextStation():
	global p
	global currentStation
	currentStation += 1
	if currentStation == len(stations):
		currentStation = 0

	p.terminate() # Kill current stream

	command = "echo 'Tuning to station ' " + stations[ currentStation ][0] + " | festival --tts"
	print command
	os.system( command )

	p = Popen(['mplayer' , '-quiet', '-playlist',stations[ currentStation ][1] ])

# Start proces

setVolume(volumeLevel) # Set start volume

bus = smbus.SMBus(1)   # Define I2C bus no ( 0 for rev A , 1 for rev B )

#os.system("echo 'Tuning first channel' | festival --tts")

# Config the radio stations array

stations = []

stations.append( ['Radio Two' , 'http://www.bbc.co.uk/radio/listen/live/r2.asx'])
stations.append( ['Radio Four', 'http://www.bbc.co.uk/radio4/wm_asx/aod/radio4_lw.asx'])
stations.append( ['Radio Three' , 'http://www.bbc.co.uk/radio/listen/live/r3.asx'])
stations.append( ['Radio Four Extra' , 'http://www.bbc.co.uk/radio/listen/live/r4x.asx'])
stations.append( ['BBC World Service' , 'http://www.radiofeeds.co.uk/ws.asx'])
stations.append( ['Five Live' , 'http://bbc.co.uk/radio/listen/live/r5l.asx'])
stations.append( ['File Live Sports Extra' , 'http://bbc.co.uk/radio/listen/live/r5lsp.asx'])
stations.append( ['Radio Merseyside' , 'http://wmlive-lracl.bbc.co.uk/wms/england/lrmerseyside'])
stations.append( ['City Talk' , 'http://tx.whatson.com/icecast.php?i=citytalk.mp3.m3u'])
stations.append( ['Radio City' , 'http://tx.whatson.com/icecast.php?i=city.mp3.m3u'])

# Start first radio stream

command = "echo 'Tuning to station ' " + stations[0][0] + " | festival --tts"
print command
os.system( command ) 

#time.sleep(10)

p = Popen(['mplayer' , '-quiet', '-playlist',stations[0][1] ]) 

delay = 0.3

bus.write_byte_data(0x20,0x00,0xff) # input
bus.write_byte_data(0x20,0x01,0xff) # input

bus.write_byte_data(0x20,0x0C,0xff)

while 1: 
	a = bus.read_byte_data(0x20,0x12)
	print "a = " + str(a)
	time.sleep(delay)

	if a == nextStationButton:
		nextStation()

	if a == upVolumeButton:
		upVolume()
	
	if a == downVolumeButton:
		downVolume()


