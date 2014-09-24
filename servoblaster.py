#!/usr/bin/env python
#
#
# Drives Servoblaster controlled servo
# https://github.com/richardghirst/PiBits/tree/master/ServoBlaster
#


import time

# From /dev/servoblaster.cfg:
# Servo Channel 0 => GPIO 4
servoChannel = 2

def setServo(servoChannel, position):
    servoStr ="%u=%u" % (servoChannel, position)
    print servoStr
    
    with open("/dev/servoblaster", "w") as f:
        f.write(servoStr)
    
    return
        
                
    

if __name__ == '__main__':
    while True:
        for i in range(50, 250):
            setServo(servoChannel, i)
            time.sleep(.1)
        

