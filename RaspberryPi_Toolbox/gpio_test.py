#!/usr/bin/env python


import RPi.GPIO as GPIO
import time

if 1:
    # Blink an LED
    pin = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    while True:
        GPIO.output(pin, GPIO.LOW)
        time.sleep(.5)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(.5)
    
    
    

