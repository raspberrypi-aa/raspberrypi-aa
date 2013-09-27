#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 2- Beginner
#    a) Reaction Timer
#
# LED on Pin 18
# Switch w/ pull up resistor on pin 4
#
# Extra: Report running average
#


import RPi.GPIO as GPIO
import time
import random

ledPin = 18
switchPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(switchPin, GPIO.IN)

rtimes = []

while True:
    print "Starting soon..."
    time.sleep(random.random()*10)    
    
    
    start_time = time.time()
    GPIO.output(ledPin, GPIO.HIGH)
    
    GPIO.wait_for_edge(switchPin, GPIO.FALLING)
    
    end_time = time.time()
    GPIO.output(ledPin, GPIO.LOW)
    
    reaction_time = end_time - start_time
    print "Reaction Time: " + str(reaction_time)
    rtimes.append(reaction_time)
    print "Average Time: " + str(1.0*sum(rtimes)/len(rtimes))
    time.sleep(5)
    
    

    
    


