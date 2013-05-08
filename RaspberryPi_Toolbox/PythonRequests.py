#!/usr/bin/env python

import requests

r = requests.get('http://google.com')
print r.text