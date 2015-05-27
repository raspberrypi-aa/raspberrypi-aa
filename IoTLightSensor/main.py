#!/usr/bin/env python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap        
app = Flask(__name__, static_folder='static', static_url_path='')

import json
cred  = dict()
with open('credentials') as f:
    cred = json.load(f)


# 
# Analog to Digital Converter Code
#
from MCP3008 import *  
adcDevice = 0
adcChannel = 0
adc = MCP3008(device=adcDevice)
@app.route("/")
def index():
    return render_template('index.html',
        homePage = True,
        page_title = "Home Page",
        light = adc.read(adcChannel))
    
    
#
# SMS Sending Code
#
from twilio.rest import TwilioRestClient, exceptions
sms = TwilioRestClient(cred['account_sid'], cred['auth_token'])    
@app.route("/testSMS")
def testSMS():
    level = adc.read(adcChannel)
    msg = sms.messages.create(to=cred['to_num'], 
        from_ = cred['from_num'], 
        body = "Light Level: "+str(level))

    return render_template('index.html',
        homePage = True,
        page_title = "Home Page",
        light = level,
        successMsg = "Text Sent!")            

#
# Motor Control Code
# 
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
motorPin = 18
freq = 1000
GPIO.setup(motorPin, GPIO.OUT, GPIO.LOW)
motor = GPIO.PWM(motorPin, freq)
motor.stop()

@app.route("/startMotor")
def startMotor():
    motor.start(0)
    for i in range(0, 100):
        motor.ChangeDutyCycle(i)
        time.sleep(.03)
        
    for i in range(100, 0, -1):
        motor.ChangeDutyCycle(i)
        time.sleep(.03)
    motor.ChangeDutyCycle(100)
        
    return render_template('index.html',
        homePage = True,
        page_title = "Home Page",
        light = "Unknown",
        successMsg = "Motor On")     

@app.route("/stopMotor")
def stopMotor():
    motor.stop()
    return render_template('index.html',
        homePage = True,
        page_title = "Home Page",
        light = "Unknown",
        successMsg = "Motor Off")         

if __name__ == "__main__":
    try:
        app.debug = True
        Bootstrap(app)
        app.run(host="0.0.0.0")        
        
    finally:
        adc.close()
        GPIO.cleanup()
        