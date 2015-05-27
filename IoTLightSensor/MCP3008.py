#!/usr/bin/env python 


import spidev

class MCP3008:
    def __init__(self, bus=0, device=0):
        ''' Creates object to read MCP3008 ADC chip at given bus address.'''
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
    

    def close(self):
        self.spi.close()
        
    def buildReadCommand(self, channel):
        start = 1
        singleEnded = 1
        return [0x00, 0x00 | (channel<<2) | (singleEnded <<5) | (start<<6), 0x00]
        
    
    def processAdcValue(self, result):
        return (result[1] & 0x03) + result[2]
    
    def read(self, channel):
        if (channel < 0 or channel > 7):
            raise IOException("Bad channel number")
        
        result = self.spi.xfer2(self.buildReadCommand(channel))
        return self.processAdcValue(result)
        
        
if __name__ == "__main__":
    import time
    try:
        spi = MCP3008(0,0)
        while True:
            print "ADC Value: " + str(spi.read(0))
            time.sleep(.5)
    except KeyboardInterrupt:
        print "Exiting..."
    finally:
        spi.close()