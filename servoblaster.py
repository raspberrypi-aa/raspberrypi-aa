#!/usr/bin/env python
#
#
# Drives Servoblaster controlled servo
# https://github.com/richardghirst/PiBits/tree/master/ServoBlaster
#


import time

# From /dev/servoblaster.cfg:
# Servo Channel 0 => GPIO 4
servoChannel = 0

def setServo(servoChannel, position):
    servoStr ="%u=%u\n" % (servoChannel, position)
    with open("/dev/servoblaster", "wb") as f:
        f.write(servoStr)
    

if __name__ == '__main__':
    while True:
        for i in range(80, 250):
            setServo(servoChannel, i)
            time.sleep(.1)
        

