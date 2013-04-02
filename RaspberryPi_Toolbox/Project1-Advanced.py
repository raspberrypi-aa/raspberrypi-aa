#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 1 - Advanced
#    Use a 74HC595 shift register to implement an R-2R DAC
#


clkPin = 0
dataPin = 0
latchPin = 0

regContents = [GPIO.LOW]*8

def setupShiftReg(srClk, ser, rClk):
    'crClk = serial clock, ser = serial, rClk = latch clock'
    GPIO.setup(srClk, GPIO.OUT)
    GPIO.setup(ser, GPIO.OUT)
    GPIO.setup(rClk, GPIO.OUT)
    
def writeShiftReg(regContents, clkPin, dataPin, latchPin):
    '''clkPin=>SRCLK
       dataPin=>SET
       latchPin=>RCLK
    '''
    GPIO.output(latchPin, GPIO.LOW)
    for r in regContents:
        
        GPIO.output(clkPin, GPIO.LOW)
        GPIO.output(dataPin, r)
        GPIO.output(clkPin, GPIO.HIGH)
        GPIO.output(latchPin, GPIO.HIGH)


def setVoltage(val):
    
    writeShifReg(regContents, clkPin, dataPin, latchPin)
    