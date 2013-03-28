import RPi.GPIO as GPIO
import time
    
if 1:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)  
    
# Blink an LED
if 1:
    pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    while True:
        print "On"
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(.5)
        print "Off"
        GPIO.output(pin, GPIO.LOW)
        time.sleep(.5)
    
  
    
    

