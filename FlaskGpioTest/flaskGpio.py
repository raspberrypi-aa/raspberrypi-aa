#!/usr/bin/env python
#
# Artisan's Asylum - Introduction to Raspberry Pi
# GPIO Tester
try:
  import RPi.GPIO as GPIO
except RuntimeError:
  print "Need to run with superuser permissions to access GPIO"


def setupGPIO():
  '''Before using the GPIO Pins, set the numbering mode.
    Hint: use board numbering here'''
  return 0

def changePinDir(pinNumber):
  ''' Set the pin direction to either IN or OUT'''
  if pinState[pinNumber]['direction'] == "None":
#    GPIO.setup(pinNumber, GPIO.IN, GPIO.LOW)


      changePinState(pinNumber)
      successMsg = "Successfully changed pin" + str(pinNumber) + \
          " to " + newState
    return render_template('flaskGpioTemplate.html', 
                           successMsg=successMsg,
                           pinSet=pinState)

      
    

    
    

  return app


if __name__ == '__main__':
  try:
    create_app().run(debug = True, host="0.0.0.0")
  except KeyboardInterrupt:
    GPIO.cleanup()
  


