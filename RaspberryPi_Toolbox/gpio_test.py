import RPi.GPIO as GPIO
import time

if 0:
    # Blink an LED
    pin = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    while True:
        GPIO.output(pin, GPIO.LOW)
        time.sleep(.5)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(.5)
    
    
    
    
    

