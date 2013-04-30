#!/usr/bin/env python
#
# Bitbang'd SPI interface with an MCP3008 ADC device
# MCP3008 is 8-channel 10-bit analog to digital converter
#  Connections are:
#     CLK => SCLK  
#     DOUT =>  MISO
#     DIN => MOSI
#     CS => CE0 

import time
import sys
import spidev

spi = spidev.SpiDev()
spi.open(0,0)

def buildReadCommand(channel):
    startBit = 0x01
    singleEnded = 0x08
    
    return [startBit, singleEnded|(channel<<4), 0]
    
def processAdcValue(result):
    '''Take in result as array of three bytes. 
       Return the two lowest bits of the 2nd byte and
       all of the third byte'''
       byte2 = (r[1] & 0x03)
      
       return (byte2 << 8) | r[2]
    
        
def readAdc(channel):
    if ((channel > 7) or (channel < 0)):
        return -1
    r = spi.xfer2(buildReadCommand(channel))
    adcout = ((r[1]&3) << 8) + r[2]
    return adcout    
        
if __name__ == '__main__':
    try:
        while True:
            val = readAdc(0)
            print "ADC Result: ", str(val)
            time.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)