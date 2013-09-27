import RPi.GPIO as GPIO
import time
    
# Blink an LED
if 0:
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
    

# Poll for input
if 0:
    input_pin = 4 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_pin, GPIO.IN)  
    while True:
        input_val = GPIO.input(input_pin)
        print "value: "+str(input_val)
        time.sleep(.5)
        
if 1:
    input_pin = 4 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_pin, GPIO.IN) 
    GPIO.add_event_detect(input_pin, GPIO.FALLING)
    while True:
        if GPIO.event_detected(input_pin):
            print True
        else:
            print False
        time.sleep(.5)
    
    
    

