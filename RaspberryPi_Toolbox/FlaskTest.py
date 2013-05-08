#!/usr/bin/env python

import flask
from flask import Flask

# Create the server
app = Flask(__name__)

# Define handlers for each path
@app.route('/')
def root():
    return "Hello World"
    
# Test with: curl http://localhost:5000/echoParam?k=v\&k1=v1
@app.route('/echoParam')
def echoParam():
    return str(flask.request.args)
        
    
@app.route('/postTest', methods=['POST'])
def postTest():
    return str(flask.request.form)
    

if __name__ == '__main__':
    app.debug = True
    app.run() # Host parameter needed to make it listen on external interface
    
    



    