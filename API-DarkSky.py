#!/usr/bin/env python

import requests
import json

api_url="https://api.forecast.io/forecast/%s/%f,%f"
api_key="95e520f32344fbe069d37ca9279d224e"
lat=42.38205
long=-71.10517

query_url = api_url % (api_key, lat, long)
print query_url

r = requests.get(query_url)
if r.status_code != 200:
  print "Error:", r.status_code

#print r.text
print "---"
print json.dumps(r.json(),
	sort_keys = True,
	indent=4)

currentWeather =  r.json()['currently']['icon']
if "cloud" in currentWeather:
  print "Cloudy"
elif "rain" in currentWeather:
  print "Rain"
else:
  print "Clear"

