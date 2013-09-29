#!/usr/bin/env python
#
# stopwatch.py
#

import RPi.GPIO as GPIO
import time

LED = 18
SWITCH = 4

GPIO.setmode(GPIO.BCM)		# Set to board numbering
GPIO.setup(LED, GPIO.OUT)	# Setup LED channel for output
GPIO.setup(SWITCH, GPIO.IN)	# Setup switch channel for input
GPIO.output(LED, GPIO.LOW)	# Initialize output state to low

# Preserve system resources with sleep() by preventing constant polling for input
while True:
    while GPIO.input(SWITCH) == GPIO.HIGH:	# Sleep while button released
        time.sleep(.02)
    # When button is pressed, exit while loop
	start_time = time.time()				# Store current time
    print "Started Timer"
    GPIO.output(LED, GPIO.HIGH)				# Turn on LED
    while GPIO.input(SWITCH) == GPIO.LOW:	# Sleep while button pressed
        time.sleep(.02)
    while GPIO.input(SWITCH) == GPIO.HIGH:	# Sleep while button released
        time.sleep(.02)
    GPIO.output(LED, GPIO.LOW)				# Turn off LED
    end_time = time.time()
    print "Stopped Timer"
    print "Time: " + str(end_time - start_time)

