#!/usr/bin/env python

from flask import Flask

# Create the server
app = Flask(__name__)

# Define handlers for each path
@app.route('/')
def root():
    return "Hello World"
    
@app.route('/echoParam')
def echoParam():
    print request.args
        
    
@app.route('/postTest', methods=['POST'])
def postTest():
    return request.form['key']
    

if __name__ == '__main__':
    app.run() # Host parameter needed to make it listen on external interface
    
    



    