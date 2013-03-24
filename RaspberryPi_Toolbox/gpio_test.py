import RPi.GPIO as GPIO
import time

if 1:
    # Blink an LED
    pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    while True:
        GPIO.output(pin, GPIO.LOW)
        time.sleep(.5)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(.5)
    
    
    
    
    

