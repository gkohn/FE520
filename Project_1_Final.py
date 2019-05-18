# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:12:22 2019

@author: grace.kohn
"""

import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='grace.kohn', api_key='EfF1k1qm9XVtAxoC79e7')

df = pd.read_csv("Data.csv")

df_mil = df[df['Age'] == '21-35']
df_x = df[df['Age'] == '36-51']
df_boom = df[df['Age'] == '52-70']

trace_reset = go.Histogram(y=df['Level of Robo'], name = 'All')
trace_millenial = go.Histogram(y=df_mil['Level of Robo'], name = 'Millenial')
trace_x = go.Histogram(y=df_x['Level of Robo'], name = 'Gen X')
trace_boom = go.Histogram(y=df_boom['Level of Robo'], name = 'Baby Boomer')

data = [trace_reset, trace_millenial, trace_x, trace_boom]

layout = dict(title='Sample Population Advisor Type', showlegend=False,)

fig = dict(data=data, layout=layout)
py.plot(fig, filename='update_dropdown')