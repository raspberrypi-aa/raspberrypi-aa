#!/usr/bin/env python

import requests
import sys

# Making a simple request
if False:
    r = requests.get('http://google.com')
    print r.text
    print r.status_code
    print r.headers
    sys.exit(0)

# Passing parameters to the request
if True:
    searchTerms = {'q' : 'raspberry Pi'} 
    r = requests.get('http://google.com/search', 
                params=searchTerms)
    print r.content
    print r.status_code
    
# Setting headers
if True:
    searchTerms = {'X-Platform' : 'raspberryPi'} 
    r = requests.get('http://google.com/', headers=searchTerms)
    print r.content
    print r.status_code

#Basic auth
if False:
  r = requests.get('http://abcd.com', auth=('user', 'pass'))
