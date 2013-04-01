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

def genSeq(length):
    '''Generate a sequence (ledPin, switchPin) of given length'''
    retList = []
    for x in xrange(0, length):
        r = r.randomInt(0, len(ledPin))
        retList.append((ledPin[r], switchPin[r]))

def get_next_pin_low(pinList, timeout):
    '''Sit in while loop until any pin in pinList goes low. If no pin pressed
    before timeout, return false. Return number of pin pressed'''
    start_time = time.time()
    while start_time + timeout < time.time():
        for pin in pinList:
            if GPIO.input(pin) == 0:
                return pin
            time.sleep(.05)
    return False
    

def checkSeq(seq, timeout):
    '''Wait for user to enter the sequence. Return true if correct. Return
    false if wrong pin pressed or timeout reached'''
    for step in seq:
        
    

def blinkSeq(seq):
    'Blink LEDs in the correct sequence to teach player the pattern.'
    print "Correct sequence is "+seq
    for pin in seq: 
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    for pin in ledPin:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        
    for pin in switchPin:
        GPIO.setup(pin, GPIO.IN)
    
    print "Starting Simon Says"
    seqLength = 1;
    timeout = 10; # User must complete pattern in 10 seconds or its Game Over
    curSeq = genSeq(seqLength)
    blinkSeq(ledSeq)
    checkSequence(seq)
    