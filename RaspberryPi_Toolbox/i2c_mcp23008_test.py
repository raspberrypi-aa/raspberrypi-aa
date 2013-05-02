#!/usr/bin/env python
#
# Uses the MCP23008 I2C GPIO Expander 
#
#

import Adafruit_I2C as I2C

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
    
def setPinMode(pin, input):
    '''Pin is the pin number to modify input/output state of.
       Input is True to set the pin as input, False to set it as output'''
    
    direction = i2c.read(IODIR)
    
    if input:
        direction |= (1 << pin)
    else:
        direction = direction & ~(1<<pin)
        
    i2c.write(IODIR, direction)

def setPin(pin, state):
    gpio = i2c.read(GPIO)
    
    if state:
        gpio = gpio | (1 << pin)
    else:
        gpio = gpio & ~(1<<pin)
        

if __name__ == '__main__':
    setAllOutput()
    setPin(1, True)
    