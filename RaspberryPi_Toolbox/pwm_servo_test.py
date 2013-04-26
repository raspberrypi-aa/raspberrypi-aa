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
        f.write(str(enabled))

def setPwmDutyCycle(duty):
    if duty < 0:
        duty = 0
    elif duty > 100:
        duty = 100
            
    with open("/sys/class/rpi-pwm/pwm0/frequency", "w") as f:
        f.write(str(duty))

def pwmTest():
    togglePwm(True)
    
    while True:
        for i in range(0, 100, 10):
            print "Brightness:", i
            setPwmDutyCycle(i)
            time.sleep(100)
            
    togglePwm(False)
    
if __name__ == "__main__":
    pwmTest()
    