#!/usr/bin/env python
#
# Uses the MCP23008 I2C GPIO Expander 
#
#

import Adafruit_I2C as I2C
import time
import sys

#if True:
#    mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)
#    mcp.config(0, OUTPUT)
#    mcp.output(0, 1)

IODIR = 0x00 
GPIO = 0x09
GPPU = 0x06
i2c = I2C.Adafruit_I2C(address=0x20)

def setAllInput():
    i2c.write8(IODIR, 0xFF)
    
def setAllOutput():
    i2c.write8(IODIR, 0x00)
    
def setPinMode(pin, input, pullup=False):
    '''Pin is the pin number to modify input/output state of.
       Input is True to set the pin as input, False to set it as output'''
    
    direction = i2c.readU8(IODIR)
    
    if input:
        direction |= (1 << pin)
        
    else:
        direction = direction & ~(1<<pin)
        
    i2c.write8(IODIR, direction)
    
    if input:
        puReg = i2c.readU8(GPPU)
        
        if pullup:
            puReg = puReg | (1<<pin)
        else:
            puReg = puReg & ~(1<<pin)
            
        i2c.write8(GPPU, puReg)
        print "pullup"
        print i2c.readU8(GPPU)        

def setPin(pin, state):
    gpio = i2c.readU8(GPIO)
    
    if state:
        gpio = gpio | (1 << pin)
    else:
        gpio = gpio & ~(1<<pin)
        
    i2c.write8(GPIO, gpio)

def readPin(pin):
    gpio = i2c.readU8(GPIO)
    return (gpio >> pin) & 0x01

if __name__ == '__main__':
    try:
        setAllOutput()
        setPinMode(1, True, True)
        
        print "IODIR"
        print i2c.readU8(IODIR)
        setPin(7, False)
        print "GPIO"
        print i2c.readU8(GPIO)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
    