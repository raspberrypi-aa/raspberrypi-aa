#!/usr/bin/env python
#
# Demonstrates Servo control 
# 
# MUST use pin 18

import time


def toggleServo(enabled): 
    value = "0"
    if enabled:
        value = "1"
        
    with open("/sys/class/rpi-pwm/pwm0/active", "w") as f:
        f.write(value)
        

# Duty cycle can vary between 1-180
def setServoPosition(pos):
    if duty <= 0:
        duty = 1
    elif duty > 180:
        duty = 180
            
    with open("/sys/class/rpi-pwm/pwm0/servo", "w") as f:
        f.write(str(duty))

def pwmTest():
    setPwmFrequency()
    togglePwm(True)
    
    while True:
        for i in range(0, 100, 1):
            print "Brightness:", i
            setPwmDutyCycle(i)
            time.sleep(.01)
            
    togglePwm(False)
    
if __name__ == "__main__":
    pwmTest()
    