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
        f.write("2=249")
    
    return
        
                
    

if __name__ == '__main__':
    setServo(servoChannel, 249)
        

