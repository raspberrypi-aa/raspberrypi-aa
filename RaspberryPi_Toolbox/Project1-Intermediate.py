#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 1 - Intermediate
# Simon Says
#
# LED on Pin 14, 15, 18
# Switches w/ internal pull up resistor on pin 4, 17, 21


import RPi.GPIO as GPIO
import time
import random

ledPin = [14, 15, 18]
switchPin = [4, 17, 21]

def genSeq(length):
    '''Generate a tuple of sequences ([ledPins], [switchPins]) of given length'''
    ledPins = []
    switchPins = []
    for x in xrange(0, length):
        r = r.randomInt(0, len(ledPin))
        ledPins.append(ledPin[r])
        switchPins.append(switchPin[r])
    return (ledPins, switchPins)

def get_next_pin_low(pinList, timeout):
    '''Sit in while loop until timeout is reached. Use a for loop to check 
    the input state of each switch Pin, returning the pin number if it is 
    pressed (Low). Sleep for 5ms between checking each pin to avoid using
    up all the CPU time'''
    #
    # IMPLEMENT THIS FUNCTION
    #

    

def checkSeq(seq, timeout):
    '''Wait for user to enter the sequence. Return true if correct. Return
    false if wrong pin pressed or timeout reached'''
    for step in seq:
        if get_next_pin_low(switchPin, timeout) != step
            return False
    return True
    

def blinkSeq(seq):
    'Blink LEDs in the correct sequence to teach player the pattern.'
    print "Correct sequence is "+seq
    #
    # IMPLEMENT THIS FUNCTION
    #

def setup():
    '''Set to mode to BCM. Set each ledPin to output and state LOW. 
    Setup each input pin, configuring the Pull Up resistor if using'''
    #
    # IMPLEMENT THIS FUNCTION
    #

if __name__ == '__main__':

    setup()
    
    print "Starting Simon Says"
    seqLength = 1;
    timeout = 10; # User must complete pattern in 10 seconds or its Game Over
    curSeq = genSeq(seqLength)
    blinkSeq(curSeq[0])
    if checkSequence(curSeq[1]):
        print "Correct!"
    else:
        print "Wrong!"