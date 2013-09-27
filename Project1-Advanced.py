#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# Project 1 - Advanced
#    Use a 74HC595 shift register to implement an R-2R DAC
#
# Connections:
#   74HC595
#      Pin 8 - GND
#      Pin 10 - Serial Clear - Tie to GND (could add GPIO pin and set to high to reset)
#      Pin 11 - Serial Clk - Rising edge of clock pulse shifts new value (from SER pin) in to register
#      Pin 12 - Register Clk - (i.e. latch pin) Set to low when changing, set back to high for changes to take effect
#      Pin 13 - Output Enable - Tie to GND
#      Pin 14 - Serial Data - Rising edge of Serial Clk pulse reads in value of this pin
#      Pin 16 - Vcc - Tie to 3.3V

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
       
       This function prints least significant bit first (i.e. r[7] first)
    '''
    GPIO.output(latchPin, GPIO.LOW)
    
    for r in regContents:
        print r
        GPIO.output(clkPin, GPIO.LOW)
        GPIO.output(dataPin, r)
        GPIO.output(clkPin, GPIO.HIGH)
    
    GPIO.output(latchPin, GPIO.HIGH)


GPIO.setmode(GPIO.BCM)
regContents[7] = GPIO.HIGH
setupShiftReg(clkPin, dataPin, latchPin)
writeShiftReg(regContents, clkPin, dataPin, latchPin)

while True:
    time.sleep(1)
    