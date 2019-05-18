# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:55:07 2019

@author: grace.kohn
"""

import pandas as pd
import plotly
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='grace.kohn', api_key='EfF1k1qm9XVtAxoC79e7')

df = pd.read_csv("Data2.csv")
df_age = df[df['Category'] == 'Age']
df_model = df[df['Category'] == 'FA Model']
df_ratings = list(df.columns)[2:]

trace1 = go.Bar(
            x=list(df_ratings),
            y=list(df_age.iloc[0,2:]),
            name = 'Milennial')

trace2 = go.Bar(
            x=list(df_ratings),
            y=list(df_age.iloc[1,2:]),
            name = 'Gen X')

trace3 = go.Bar(
            x=list(df_ratings),
            y=list(df_age.iloc[2,2:]),
            name = 'Boomer')

trace4 = go.Bar(
            x=list(df_ratings),
            y=list(df_model.iloc[0,2:]),
            name = 'Dedicated FA')

trace5 = go.Bar(
            x=list(df_ratings),
            y=list(df_model.iloc[1,2:]),
            name = 'Partially Assisted')

trace6 = go.Bar(
            x=list(df_ratings),
            y=list(df_model.iloc[2,2:]),
            name = 'Hybrid Plus')

trace7 = go.Bar(
            x=list(df_ratings),
            y=list(df_model.iloc[3,2:]),
            name = 'Robo Only')


#data = [trace1, trace2]
#layout = go.Layout(barmode='group',
#                   title = 'Level of Satisfaction with Current Advisory Relationship'
#)

fig = tools.make_subplots(rows=1, cols=2)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 1)
fig.append_trace(trace3, 1, 1)
fig.append_trace(trace4, 1, 2)
fig.append_trace(trace5, 1, 2)
fig.append_trace(trace6, 1, 2)
fig.append_trace(trace7, 1, 2)

py.plot(fig, filename='basic-bar')