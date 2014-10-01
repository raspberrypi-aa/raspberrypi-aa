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
        print "Starting up Plot.ly, please wait"
        
        with open('./config.json') as config_file:
            plotly_user_config = json.load(config_file)
            pltly.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

        tempTrace = Scatter(
           x=[],
           y=[],
           name='Temperature [deg C]',
           stream = {'token': plotly_user_config["plotly_streaming_tokens"][0], 
                     'maxpoints': 100},
            yaxis='y'
        )
        
        presTrace = Scatter(
           x=[],
           y=[],
           name='Pressure [kPa]',
           stream = {'token': plotly_user_config["plotly_streaming_tokens"][1], 
                     'maxpoints': 100},
            yaxis='y2'
        )
        
        data = Data([tempTrace, presTrace])
        layout = Layout(title='Raspberry Pi Temp/Pressure Graph',
                        yaxis=YAxis(title='deg C', range=[0, 50]),
                        yaxis2=YAxis(title='kPa', overlaying='y', side='right',
                                    range=[100.87, 101.085])
    
        fig = Figure(data=data, layout=layout)
        plot_url = pltly.plot(fig, filename='Raspberry Pi Streaming Example')
        
        self.tempStream = pltly.Stream(plotly_user_config["plotly_streaming_tokens"][0])
        self.tempStream.open()
        
        self.presStream = pltly.Stream(plotly_user_config["plotly_streaming_tokens"][1])
        self.presStream.open()
        
        print "--Ready to go!"
                        
                            
        

    def addTemperaturePressure(self, temp, pressure):
        x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.tempStream.write({'x': x, 'y': temp})
        self.presStream.write({'x': x, 'y': pressure})

