#!/usr/bin/env python
#
# Demonstrates Servo control 
# 
# MUST use pin 18

import time

def setServoMode():
    with open("/sys/class/rpi-pwm/pwm0/mode", "w") as f:
        f.write("servo")    

def toggleServo(enabled): 
    value = "0"
    if enabled:
        value = "1"
        
    with open("/sys/class/rpi-pwm/pwm0/active", "w") as f:
        f.write(value)
        

# Duty cycle can vary between 1-180
def setServoPosition(pos):
    if pos <= 0:
        pos = 1
    elif pos > 180:
        pos = 180
            
    with open("/sys/class/rpi-pwm/pwm0/servo", "w") as f:
        f.write(str(pos))

def servoTest():
    setServoMode()
    toggleServo(True)
    
    while True:
        for i in range(0, 180, 1):
            print "Servo position (degrees): ",i
            setServoPosition(i)
            time.sleep(.01)
            
    toggleServo(False)
    
if __name__ == "__main__":
    servoTest()
    