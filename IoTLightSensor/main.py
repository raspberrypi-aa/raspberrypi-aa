#!/usr/bin/env python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap        
import MCP3008.MCP3008 as MCP3008


adc = MCP3008(0, 0)
app = Flask(__name__, static_folder='static', static_url_path='')
adcChannel = 0


@app.route("/")
def index():
    return render_template('index.html',
        homePage = True,
        page_title = "Home Page",
        light = adc.read(adcChannel))
    


if __name__ == "__main__":
    try:
        app.debug = True
        Bootstrap(app)
        app.run(host="0.0.0.0")        
        
    finally:
        adc.close()
        






