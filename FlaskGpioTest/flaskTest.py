#!/usr/bin/env python
from flask import Flask
import RPi.GPIO as GPIO


# Create the server
app = Flask(__name__)


@app.route('/gpio/<int:pin>/on')
def gpio_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return "Turned pin " + str(pin) + "on"

@app.route('/gpio/<int:pin>/off')
def gpio_off(pin):
    GPIO.output(pin, GPIO.LOW)
    return "Turned pin " + str(pin) + "off"

if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)        
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        
        app.debug = True
        app.run(host="0.0.0.0")
    except KeyboardInterrupt:
       GPIO.cleanup()