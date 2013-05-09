#!/usr/bin/env python
import requests
import json
from requests_oauthlib import OAuth1

auth_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
post_url = 'https://api.twitter.com/1.1/statuses/update.json'

auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 
    'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

requests.get(auth_url, auth=auth)


