#!/usr/bin/env python

import picamera

cam = picamera.PiCamera()

try:
    cam.capture("now.jpg")
finally:
    cam.close()
    
    


