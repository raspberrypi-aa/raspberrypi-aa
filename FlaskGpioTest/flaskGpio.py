#!/usr/bin/env python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import datetime
import sys

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

# TODO: Add a handler for the path "/test" here

  @app.route('/lighting')
  def lighting():
     lightingData={'active': GPIO.input(LAMP_PIN)}
     return render_template('flaskGpioTemplate.html', page_title="Lighting", lighting=lightingData)
  
  @app.route('/lighting/on')
  def lighting_on():
    """Turn the lamp on by setting LAMP_PIN to high. """
# TODO: Set LAMP_PIN output to high
    lightingData={}
    lightingData['active'] = True
    return render_template('flaskGpioTemplate.html', page_title="Lighting", lighting=lightingData) 

  @app.route('/lighting/off')
  def lighting_off():
    """Turn the lamp off by setting LAMP_PIN to low. """
# TODO: Set LAMP_PIN output to low
    lightingData={}
    lightingData['active'] = False
    return render_template('flaskGpioTemplate.html', page_title="Lighting", lighting=lightingData)       

  @app.route('/appliances')
  def appliances():
    applianceData = {}
    applianceData['dryer'] = False
# TODO: Check state of the DRYER_PIN input and update applianceData['dryer'] if needed
    return render_template('flaskGpioTemplate.html', page_title="Appliances", appliances=applianceData)

  def coffee_on():
    """ Turn the coffee pin on"""
    print "Coffee Maker On!"
    GPIO.output(COFFEE_PIN, GPIO.HIGH)

  @app.route('/appliances/coffee/set')
  def coffee_set():
    """" Schedule a timer to turn the coffee pin on at the specified time """

# TODO: If there is already another timer set, delete that timer and start a new one
    applianceData = {}
    applianceData['coffee'] = True
    return render_template('flaskGpioTemplate.html', page_title="Appliances", appliances=applianceData) 

  @app.route('/appliances/coffee/stop')
  def coffee_stop():
    """" Stop timer if one is running """
# TODO: Stop coffeeTimer is one is running, make sure the output is turned off

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

# TODO: Check if any events have been detected on the doorbell pin, set exterior['doorbell'] if so
    return render_template('flaskGpioTemplate.html', page_title="Exterior", exterior=exterior)

  return app


def setupPins():
# TODO: Setup the pins following the instructions. When complete, this should be the state
#  - GPIO is in Broadcom mode
#  - Output pins (initial state low): LAMP_PIN, COFFEE_PIN
#  - Input Pin: DRYER_PIN
  pass

def setupDoorbellPin():
# TODO: Setup DOORBELL_PIN as an input with an event trigger on GPIO.FALLING
  pass

def mailboxCallback(pin):
  global lastMailboxPush
  lastMailboxPush = datetime.datetime.now().strftime("%c")
  
def setupMailboxPin():
# TODO: Setup MAILBOX_PIN as an input with an event trigger on GPIO.FALLING 
#       and a callback function of mailboxCallback
  pass

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
  


