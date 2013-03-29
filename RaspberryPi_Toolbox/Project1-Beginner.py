#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 1 - Beginner
#    a) Timed LED Blink
#    b) Stopwatch
#
# LED on Pin 18
# Switch w/ pull resistor on pin 4
import RPi.GPIO as GPIO
import time

ledPin = 18
switchPin = 4
    
# Set to board numbering    
GPIO.setmode(GPIO.BCM)

# Configure LED Pin for output, initialized to off (LOW) state
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

if 0:
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(4)
        
GPIO.setup(switchPin, GPIO.IN)
while True:
    while GPIO.input(switchPin) == 1:
        pass
    start_time = time.time()
    while GPIO.input(switchPin) == 0:
        pass
    while GPIO.input(switchPin) == 1:
        pass
    end_time = time.time()
    print "Time: " + str(end_time - start_time)
    
        
    
    


    
