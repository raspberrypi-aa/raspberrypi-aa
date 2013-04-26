#!/usr/bin/env python
#
# Demonstrates PWM and Servo control 
# 
# MUST use pin 18

import time


def togglePwm(enabled): 
    value = "0"
    if enabled:
        value = "1"
        
    with open("/sys/class/rpi-pwm/pwm0/active", "w") as f:
        f.write(value)
        
def setPwmFrequency(freq=1000):
    with open("/sys/class/rpi-pwm/pwm0/frequency", "w") as f:
        print str(freq)
        f.write(str(freq))
    

def setPwmDutyCycle(duty):
    if duty < 0:
        duty = 0
    elif duty > 100:
        duty = 100
            
    with open("/sys/class/rpi-pwm/pwm0/duty", "w") as f:
        f.write(str(duty))

def pwmTest():
    setPwmFrequency()
    togglePwm(True)
    
    while True:
        #for i in range(0, 100, 1):
        #    print "Brightness:", i
        #    setPwmDutyCycle(i)
        #    time.sleep(.25)
        setPwmDutyCycle(10)
            
    togglePwm(False)
    
if __name__ == "__main__":
    pwmTest()
    