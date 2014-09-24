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
  #  servoStr ="%u=%u" % (servoChannel, position)
   # print servoStr
    f = open("/dev/servoblaster", "wb")
    f.write("2=249")
    f.close()
    
                
    

if __name__ == '__main__':
    setServo(servoChannel, 249)
        

