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

@app.route("/")
def index():
    current = readWeatherSensors()
    return render_template('index.html',
                           homePage = True,
                           page_title = "Home Page",
                           temp = current['temp'],
                           pressure = current['pressure'])
                           
                           
                           
@app.route("/temp")
def temp():
    return render_template('index.html',
                           tempPage = True,
                           page_title = "Past Temperatures")    

@app.route("/pressure")
def pressure():
    return render_template('index.html',
                           pressurePage = True,
                           page_title = "Past Pressures")

import requests
import json
@app.route("/forecast")
def forecast():
    api_url="https://api.forecast.io/forecast/%s/%f,%f"
    api_key="95e520f32344fbe069d37ca9279d224e"
    lat=42.38205
    long=-71.10517
    query_url = api_url % (api_key, lat, long) 
    r = requests.get(query_url)
    if r.status_code != 200:
        print "Error:", r.status_code
    print json.dumps(r.json(),
       sort_keys = True,
       indent=4)
    forecast =  r.json()['daily']['icon']
    return render_template('index.html',
                           forecastPage = True,
                           page_title = "Forecast",
                           forecast=forecast)

if __name__ == "__main__":
    app.debug = True
    Bootstrap(app)
    app.run(host="0.0.0.0")
