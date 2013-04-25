#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 1 - Advanced
#    Use a 74HC595 shift register to implement an R-2R DAC
#

import RPi.GPIO as GPIO
import time

clkPin = 4
dataPin = 18
latchPin = 15

regContents = [GPIO.HIGH]*8

def setupShiftReg(srClk, ser, rClk):
    'srClk = serial clock, ser = serial, rClk = latch (i.e register) clock'
    GPIO.setup(srClk, GPIO.OUT)
    GPIO.setup(ser, GPIO.OUT)
    GPIO.setup(rClk, GPIO.OUT)
    GPIO.output(srClk, GPIO.LOW)
    GPIO.output(ser, GPIO.LOW)
    GPIO.output(rClk, GPIO.LOW)
    
def writeShiftReg(regContents, clkPin, dataPin, latchPin):
    '''clkPin=>SRCLK
       dataPin=>SET
       latchPin=>RCLK
    '''
    GPIO.output(latchPin, GPIO.LOW)
    
    for r in regContents:
        print r
        GPIO.output(clkPin, GPIO.LOW)
        GPIO.output(dataPin, r)
        GPIO.output(clkPin, GPIO.HIGH)
    
    GPIO.output(latchPin, GPIO.HIGH)


GPIO.setmode(GPIO.BCM)
regContents[7] = GPIO.LOW
setupShiftReg(clkPin, dataPin, latchPin)
writeShiftReg(regContents, clkPin, dataPin, latchPin)

while True:
    time.sleep(1)
    