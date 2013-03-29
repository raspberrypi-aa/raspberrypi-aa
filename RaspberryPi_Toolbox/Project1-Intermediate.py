#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 1 - Intermediate
# Simon Says
#
# LED on Pin 14, 15, 18
# Switch w/ pull up resistor on pin 4, 17, 21


import RPi.GPIO
import time
import random

ledPin = [14, 15, 18]
switchPin = [4, 17, 21]


GPIO.setmode(GPIO.BCM)
for pin in ledPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
for pin in switchPin:
    GPIO.setup(pin, GPIO.IN)


print "Starting Simon Says"
seqLength = 1;
seq = [random() for i in range(0, seqLength)]
print "Correct sequence is "+seq
    