import plotly.plotly as pltly
from plotly.graph_objs import *

import json
import datetime

class TempPresPlotlyWrapper:
''' This class creates a scatter plot with 2 y-axis data sets
Requires config.json file in the current directory which contains key 
and stream information.

X-Axis: 
 - Time

 Y-Axis: 
 - Temperature
 - Pressue
'''    
    def __init__(self):
        with open('./config.json') as config_file:
            plotly_user_config = json.load(config_file)
            pltly.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

        url = pltly.plot([{
            'x': [],
            'y': [],
            'type': 'scatter',
            'stream': {
                'token': plotly_user_config['plotly_streaming_tokens'][0], 
                'maxpoints': 200
            }
        }], filename='Raspberry Pi Streaming Example Values')

        self.stream = pltly.Stream(plotly_user_config['plotly_streaming_tokens'][0])
        self.stream.open()

    def addTemperaturePressure(self, temp, pressure):
        x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.stream.write({'x': x, 'y': temp})

