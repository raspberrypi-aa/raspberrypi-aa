#!/usr/bin/env python

from flask import Flask, request, Response

# Create the server
app = Flask(__name__)

# Define handlers for each path
@app.route('/')
def root():
    return "Hello World"
    
# Test with: curl http://localhost:5000/echoParam?k=v\&k1=v1
@app.route('/echoParam')
def echoParam():
    try:
        return str(request.args['q'])
    except KeyError:
        return "Missing parameter"
    
import json 
@app.route('/jsonTest')
def jsonTest():
    return json.dumps({'key1': 'value1'})
    
# Template tesT:
from flask import render_template
@app.route('/template')
def template():
    
    return render_template('template_test.html',
        name='Asylum', birthday=False)
    
# Test with:  curl --data key=val --data key2=val2 -X POST http://localhost:5000/postTest
@app.route('/postTest', methods=['POST'])
def postTest():
    return str(request.form)

#
# Example of HTTP Basic Auth
# Fails with: curl -v http://localhost:5000/basic
# Works with curl --user user:pass http://localhost:5000/basic
#
from functools import wraps

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'user' and password == 'pass'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/basic')
@requires_auth
def secret_page():
    return "Authenticated Hello World"

if __name__ == '__main__':
    app.debug = True
    app.run() # Host parameter needed to make it listen on external interface
    
    



    