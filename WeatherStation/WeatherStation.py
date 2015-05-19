#!/usr/bin/env python
#
#
# To get BMP085 library:
#sudo apt-get update
#sudo apt-get install git build-essential python-dev python-smbus
#git clone https://github.com/adafruit/Adafruit_Python_BMP.git
#cd Adafruit_Python_BMP
#sudo python setup.py install
#
#

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import Adafruit_BMP.BMP085 as BMP085


app = Flask(__name__, static_folder='static', static_url_path='')
sensor = BMP085.BMP085()

def readWeatherSensors():
    return {'temp': sensor.read_temperature(),
            'pressure': sensor.read_pressure()};

#print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
#print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())

@app.route("/")
def index():
    currentx = readWeatherSensors()
    return render_template('index.html',
                           temp=current['temp'],
                           pressure = current['pressure'])
                           


if __name__ == "__main__":
    app.debug = True
    Bootstrap(app).run(host="0.0.0.0")
