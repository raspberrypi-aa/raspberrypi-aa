#!/usr/bin/env python

import time
import picamera

camera = picamera.PiCamera()

def startTimelapse(count, delay):
    pics = 0
    for x in camera.capture_continuous("/home/pi/image{counter}.jpg"):
        print "Captured %s" % (x)
        time.sleep(delay)
        pics += 1
        if (pics == count):
            break

if __name__ == '__main__':
    try:
      while True:
          count = int(raw_input("Enter number of photos to take> "))
          delay = int(raw_input("Number of seconds between photos> "))
          startTimelapse(count, delay)
          
    except KeyboardInterrupt:
        print "Exiting"
        
    finally:
        # Remember to close the camera to prevent GPU memory leaks!
        camera.close()
