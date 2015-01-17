#!/usr/bin/python

# use this instead:
# http://ubuntuforums.org/showthread.php?t=2243162&p=13127246#post13127246

import sys

minBrightness = 100;

maxBrightnessFile = open("/sys/class/backlight/intel_backlight/max_brightness", "r");
maxBrightness = int(maxBrightnessFile.read());
maxBrightnessFile.close();

brightnessFile = open("/sys/class/backlight/intel_backlight/brightness", "r+")
brightness = int(brightnessFile.read())
brightnessFile.seek(0)
brightnessFile.truncate()

try:
    step = int( sys.argv[1] );
except (IndexError, ValueError):
    step = 0;

if step > 0:
    if brightness <= ( maxBrightness - step ):
        brightness += step
    else:
        brightness = maxBrightness
elif step < 0:
    if brightness >= (minBrightness - step):
        brightness += step
    else:
        brightness = minBrightness

brightnessFile.write( str(brightness) + "\n" );
brightnessFile.close();
