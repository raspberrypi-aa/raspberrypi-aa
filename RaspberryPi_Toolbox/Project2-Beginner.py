#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 2- Beginner
#    a) Reaction Timer
#
# LED on Pin 18
# Switch w/ pull up resistor on pin 4


import RPi.GPIO as GPIO
import time
import random

ledPin = 18
switchPin = 4

GPIO.setup(ledPin, RPIO.OUT)
GPIO.setup(switchPin, RPIO.IN)

def 

while True:
    print "Starting soon..."
    time.sleep(random.random()*10)    
    
    
    start_time = time.time()
    GPIO.output(ledPin, GPIO.HIGH)
    
    GPIO.wait_for_edge(switchPin, GPIO.FALLING)
    
    end_time = time.time()
    GPIO.output(ledPin, GPIO.LOW)
    
    print "Reaction Time: " str(end_time - start_time)
    time.sleep(5)
    
    
    
    


