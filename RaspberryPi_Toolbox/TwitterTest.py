#!/usr/bin/env python
import requests
import json
from requests_oauthlib import OAuth1

auth_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
post_url = 'https://api.twitter.com/1.1/statuses/update.json'

consumer_key='92oyz9BnOjNlHDeKde0pg'
consumer_secret='WE5x2ewboavGWLYJeHbxyBxQzolBQVLcIiZLqpsgh5g'
access_token='8938062-rhlMsIq2QVQziyMKJHmU6sxfL4kcZzKKasWEVHuEq0'
access_token_secret='MCQNdiAqLJgFJ2cQftMzWodiRufUXPj7nMbbPFozpZM'


auth = OAuth1(consumer_key, consumer_secret, 
    access_token, access_token_secret)

if False:
    r = requests.get(auth_url, auth=auth)
    print r.status_code
    print r.text

if True:
    twitter_post = {'status' : 'Raspberry Pi can talk'}
    r = requests.post(post_url, auth=auth, data=json.dumps(twitter_post))
    print r.status_code
    print r.text


    