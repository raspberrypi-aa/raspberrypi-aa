#!/usr/bin/env python

import requests

# Making a simple request
if True:
    r = requests.get('http://google.com')
    print r.text
    print r.status_code
    print r.headers

# Passing parameters to the request
if True:
    searchTerms = {'q' : 'raspberryPi'} 
    r = requests.get('http://google.com/search', params=searchTerms)
    print r.content
    print r.status_code

