#!/usr/bin/env python
import requests
import json
from requests_oauthlib import OAuth1

auth_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
post_url = 'https://api.twitter.com/1.1/statuses/update.json'

consumer_key='92oyz9BnOjNlHDeKde0pg'
consumer_secret='WE5x2ewboavGWLYJeHbxyBxQzolBQVLcIiZLqpsgh5g'
access_token='8938062-wkbg4TagRKS7IJCaauvpX9LQtuX4FIsevFXWDhbkkK'
access_token_secret='8vC7Nr8cisMCRl3hRevQsoGlr0UuBZ24UMNNxe99ek'


auth = OAuth1(consumer_key, consumer_secret, 
    access_token, access_token_secret)

if False:
    r = requests.get(auth_url, auth=auth)
    print r.status_code
    print r.text

if True:
    status = "Raspberry Pi can talk"
    r = requests.post(post_url, auth=auth, data="status=%s" % (status))
    response = json.loads(r)
    print response
    print r.status_code



    