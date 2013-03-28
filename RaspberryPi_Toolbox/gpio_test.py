import RPi.GPIO as GPIO
import time
    
if 1:
    input_pin = 4 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_pin, GPIO.IN)  
    while True:
        input_val = GPIO.input(input_pin)
        print "value: "+input_val
        time.sleep(.5)
        
    
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
    
  
    
    

