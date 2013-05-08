#!/usr/bin/env python

from flask import Flask, request

# Create the server
app = Flask(__name__)

# Define handlers for each path
@app.route('/')
def root():
    return "Hello World"
    
# Test with: curl http://localhost:5000/echoParam?k=v\&k1=v1
@app.route('/echoParam')
def echoParam():
    return str(request.args)
        
    
# Test with:  curl --data key=val --data key2=val2 -X POST http://localhost:5000/postTest
@app.route('/postTest', methods=['POST'])
def postTest():
    return str(request.form)
    

if __name__ == '__main__':
    app.debug = True
    app.run() # Host parameter needed to make it listen on external interface
    
    



    