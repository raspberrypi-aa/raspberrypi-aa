#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 1 - Intermediate
# Simon Says
#
# LED on Pin 14, 15, 18
# Switch w/ pull up resistor on pin 4, 17, 21


import RPi.GPIO

ledPin = [14, 15, 18]
switchPin = [4, 17, 21]


GPIO.setmode(GPIO.BCM)
for pin in ledPin:
    
    