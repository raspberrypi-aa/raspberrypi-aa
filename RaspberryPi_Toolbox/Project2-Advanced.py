#!/usr/bin/env python
#
# Project 2 Advanced - Frequency Counter
# 


import RPi.GPIO as GPIO
import time

switchPin = 4
updateIntervalSeconds=5

counter = 0

def fallingEdge(pin):
    global counter
    counter += 1    

GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin, GPIO.IN)

GPIO.add_event_detect(switchPin, GPIO.FALLING)
GPIO.add_event_callback(switchPin, fallingEdge)

while True:
    time.sleep(updateIntervalSeconds)
    freq = counter / updateIntervalSeconds
    counter = 0
    print "Frequency: %d Hz" % (freq)
    


