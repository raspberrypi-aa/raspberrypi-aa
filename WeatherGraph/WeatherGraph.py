#!/usr/bin/env python
#
# Reads temperature and barometric pressure from BMP180 SPI sensor
# Posts results to http://plot.ly
#


import Adafruit_BMP.BMP085 as BMP085
import PlotlyWrapper

sensor = BMP085.BMP085()
plotter = PlotlyWrapper.TempPresPlotlyWrapper()

print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())