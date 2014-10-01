#!/usr/bin/env python
#
# Reads temperature and barometric pressure from BMP180 SPI sensor
# Posts results to http://plot.ly
#


import Adafruit_BMP.BMP085 as BMP085
import PlotlyWrapper
import time

sensor = BMP085.BMP085()
plotter = PlotlyWrapper.TempPresPlotlyWrapper()

print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())


for i in range(0, 10):
    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()/1000
    print 'Temp = {0:0.2f} *C'.format(temp)
    print 'Pressure = {0:0.2f} Pa'.format(pressure)
    plotter.addTemperaturePressure(temp, pressure)
    time.sleep(1)

    
    