import alsaaudio
m = alsaaudio.Mixer()   # defined alsaaudio.Mixer to change volume
m.setvolume(50) # set volume
vol = m.getvolume() # get volume float value
