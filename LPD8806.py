#!/usr/bin/python

class LPD8806:
    def __init__(self, numLeds, spiPath="/dev/spidev0.0"):
        self.begun = False
        self.pixels = []
        self.updateLength(numLeds)
        self.spiPath = spiPath
        
        if self.begun:
            self.startSPI()

    def begin(self):
        self.startSPI()
        self.begun = True
    
    def startSPI(self):
        self.spi = open(self.spiPath, 'wb')
        for x in xrange(1, (self.numLeds + 31)/32 - 1):
            self.spi.write(0)

    def updateLength(self, numLeds):
        latchBytes = (numLeds + 31) / 32 
        numBytes = numLeds * 3 + latchBytes
        self.numLeds = numLeds
        self.pixels = [0x80 for x in xrange(0, numLeds*3)]
        self.pixels.extend([0 for x in xrange(0, latchBytes)])
        
    def numPixels(self):
        return self.numLeds

    def show(self):
    	#self.spi.write("%c" % self.pixels[0])
    	#self.spi.flush()
    	#debug = open("/tmp/spidebug", 'wb')
        for x in self.pixels:
           self.spi.write("%c" % x)
           #print "%x" % (x)
        self.spi.flush()
        
	def getWheel(self, WheelPos):
		if (WheelPos < 85):
   			return self.Color(WheelPos * 3, 255 - WheelPos * 3, 0)
		elif (WheelPos < 170):
   			WheelPos -= 85;
   			return self.Color(255 - WheelPos * 3, 0, WheelPos * 3)
		else:
			WheelPos -= 170;
			return self.Color(0, WheelPos * 3, 255 - WheelPos * 3)
        
    def rainbow(self, idx):
    	if idx < 85:
    		return self.Color(idx * 3, 255 - idx * 3, 0)
    	elif (idx < 170):
    		idx -= 85
    		return self.Color(255 - idx * 3, 0, idx * 3)
    	else:
    		idx -= 170
    		return self.Color(0, idx *3, 255 - idx * 3)
    
        
    def Color(self, red, green, blue):
        return (((green | 0x80) << 16) | ((red | 0x80) << 8) | (blue | 0x80))

    def setPixelColor(self, pixelNum, color):
        if pixelNum < self.numLeds:
            self.pixels[pixelNum * 3] = (color >> 16) | 0x80
            self.pixels[pixelNum * 3 + 1] = (((color >> 8 ) & 0xFF )| 0x80)
            self.pixels[pixelNum * 3 + 2] = ((color & 0xFF) | 0x80 ) 
            print "%d %d %d" % (self.pixels[pixelNum * 3], self.pixels[pixelNum * 3+1], self.pixels[pixelNum * 3+2])
            

    def getPixelColor(self, pixelNum):
        if pixelNum < self.numLeds:
            return ((self.pixels[pixelNum * 3] & 0x7f) << 16) | ((self.pixels[pixelNum * 3 + 1] & 0x7f) << 8) | (self.pixels[pixelNum * 3 + 2] & 0x7f)
        return 0
            
if __name__ == '__main__':
  import time
  strip = LPD8806(2)
  strip.begin()
  red  = 0
  green = 0
  blue = 0
  degree = 0
    
  try:    
    while True:
      degree = (degree + 1) % 256
	
      if degree > 128:
  		degree_out = 256 - degree
      else:
  		degree_out = degree
          
      print degree_out
          
      color = strip.Color(degree_out, 0, 0)
      strip.setPixelColor(0, strip.rainbow(degree_out))
      strip.setPixelColor(1, strip.rainbow(degree_out))
      strip.show()
      time.sleep(.1)

  except KeyboardInterrupt:
      pass

