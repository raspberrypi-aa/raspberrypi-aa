#!/usr/bin/env python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import datetime
import RPi.GPIO as GPIO
import sys
import threading

LAMP_PIN = 18
COFFEE_PIN = 23
DRYER_PIN = 24
DOORBELL_PIN = 17
MAILBOX_PIN = 4

lastMailboxPush = "Never"
coffeeTimer = None

def create_app():
  app = Flask(__name__, static_folder='static', static_url_path='')
  Bootstrap(app)
  
  
  @app.route('/')
  def root():
    return render_template('flaskGpioTemplate.html', page_title="Home", home=True)

  @app.route('/test')
  def test():
     return render_template('flaskGpioTemplate.html', page_title="Home", successMsg="You clicked the button!", home=True)

  @app.route('/lighting')
  def lighting():
     lightingData={'active': GPIO.input(LAMP_PIN)}
     return render_template('flaskGpioTemplate.html', page_title="Lighting", lighting=lightingData)
  
  @app.route('/lighting/on')
  def lighting_on():
    """Turn the lamp on by setting LAMP_PIN to high. """
    GPIO.output(LAMP_PIN, GPIO.HIGH)
    lightingData={}
    lightingData['active'] = True
    return render_template('flaskGpioTemplate.html', page_title="Lighting", lighting=lightingData) 

  @app.route('/lighting/off')
  def lighting_off():
    """Turn the lamp off by setting LAMP_PIN to low. """
    GPIO.output(LAMP_PIN, GPIO.LOW)
    lightingData={}
    lightingData['active'] = False
    return render_template('flaskGpioTemplate.html', page_title="Lighting", lighting=lightingData)       

  @app.route('/appliances')
  def appliances():
    applianceData = {}
    applianceData['dryer'] = False
    if GPIO.input(DRYER_PIN):
      applianceData['dryer'] = True
    return render_template('flaskGpioTemplate.html', page_title="Appliances", appliances=applianceData)

  def coffee_on():
    """ Turn the coffee pin on"""
    print "Coffee Maker On!"
    GPIO.output(COFFEE_PIN, GPIO.HIGH)

  @app.route('/appliances/coffee/set')
  def coffee_set():
    """" Schedule a timer to turn the coffee pin on at the specified time 

    If there is already another timer set (either start or stop), delete that timer and start a new one"""
    if coffeeTimer is not None:
      coffeeTimer.cancel()
    coffeeTime = threading.Timer(30, coffee_on)
    coffeeTime.start()

    applianceData = {}
    applianceData['coffee'] = True
    return render_template('flaskGpioTemplate.html', page_title="Appliances", appliances=applianceData) 

  @app.route('/appliances/coffee/stop')
  def coffee_stop():
    """" Stop timer if one is running """
    if coffeeTimer is not None:
      coffeeTimer.cancel()
    GPIO.output(COFFEE_PIN, GPIO.LOW)
    applianceData = {}
    applianceData['coffee'] = False
    return render_template('flaskGpioTemplate.html', page_title="Appliances", appliances=applianceData) 

  @app.route('/exterior')
  def exterior():
    """ Show two pieces of information about the house's exterior.

    - Has the doorbell been pressed since the last time it was checked?
    - When was the last time the doorbell was pressed?
    """
    exterior = {'doorbell': False,
                'time_string': lastMailboxPush}

    if (GPIO.event_detected(DOORBELL_PIN)):
      exterior['doorbell'] = True

    print exterior

    return render_template('flaskGpioTemplate.html', page_title="Exterior", exterior=exterior)

  return app


def setupPins():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LAMP_PIN, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(COFFEE_PIN, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(DRYER_PIN, GPIO.IN)


def setupDoorbellPin():
  GPIO.setup(DOORBELL_PIN, GPIO.IN)
  GPIO.add_event_detect(DOORBELL_PIN, GPIO.FALLING)

def mailboxCallback(pin):
  global lastMailboxPush
  lastMailboxPush = datetime.datetime.now().strftime("%c")
  
def setupMailboxPin():
  GPIO.setup(MAILBOX_PIN, GPIO.IN)
  GPIO.add_event_detect(MAILBOX_PIN, GPIO.FALLING,
                        bouncetime=200, callback=mailboxCallback)

if __name__ == '__main__':
  try:
    setupPins()
    setupDoorbellPin()
    setupMailboxPin()
    create_app().run(debug = True, host="0.0.0.0")
  except KeyboardInterrupt:
    print "Ctrl-C hit, exiting"

  finally:
    GPIO.cleanup()
    print "Cleaned up GPIO pins"
  


