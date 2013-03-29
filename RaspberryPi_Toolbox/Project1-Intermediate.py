#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 1 - Intermediate
# Simon Says
#
# LED on Pin 14, 15, 18
# Switch w/ pull up resistor on pin 4, 17, 21

######
#XXX_EF Provide functions to student and tell them the order to write the code in
######

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


def blinkSeq(seq):
    print "Correct sequence is "+seq
    for pin in seq: 
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)

print "Starting Simon Says"
seqLength = 1;
timeout = 10; # User must complete pattern in 10 seconds or its Game Over
seq = [random() for i in range(0, seqLength)]
blinkSeq(seq)
    