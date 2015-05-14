#!/usr/bin/env python

from flask import Flask
import RPi.GPIO as GPIO

doorPin = 4
app = Flask(__name__)


@app.route("/doorStatus")
def doorStatus():
    if GPIO.event_detected(doorPin):
        return "Door has been open"
    else:
        return "Door was Closed since last check"


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(doorPin, GPIO.IN)
    GPIO.add_event_detect(doorPin, GPIO.BOTH)
    
    app.debug = True
    app.run(host="0.0.0.0")
