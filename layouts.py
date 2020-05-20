# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:30:10 2020

@author: Syamanthaka B
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import data_n_graphs as grf
from datetime import datetime as dt


## Main Home Page
##################################################################################################

body = html.Div([
    ### Heading Row
    dbc.Row(dbc.Col(html.H1("CLC KPI Dashboard", style={'text-align' : 'center'}))),
    dbc.Row(dbc.Col(html.Div(html.Hr()))),
    
    
    dbc.Row([
        ### Left Column for quadruple aims
        dbc.Col([
            html.Div("Quadruple aims"),
            dcc.Location(id='url', refresh=False),
            html.MapEl([
                html.Area(target='', alt='Aim1', title='Improved Patient Experience', href='#Aim1', coords='0,0,250,250', shape='rect'),
                html.Area(target='', alt='Aim2', title='Better Health Outcomes', href='#Aim2', coords='250,0,500,250', shape='rect'),
                html.Area(target='', alt='Aim3', title='Lower Cost of Care', href='#Aim3', coords='250,250,500,500', shape='rect'),
                html.Area(target='', alt='Aim4', title='Improved Staff Experience', href='#Aim4', coords='0,250,250,500', shape='rect'),
            ],name='map'),
            html.Img(src='assets/quad_aim.png', useMap='#map')
        ], width=4),
        
        ### Main column of graphs from annual_data
        dbc.Col([
            dbc.Row([
                
                ### Facility drop down
                html.Label(["Select Facility from the list", 
                dcc.Dropdown(
                    id='facility_select',
                    options=[{'label': i, 'value': i} for i in grf.facility],
                    value=grf.facility[0]
                )
                ]),
                
                html.Label(["Select KPI to display", 
                dcc.Dropdown(
                    id='y_axis',
                    options=[{'label': i, 'value': i} for i in grf.y_cols],
                    value=grf.y_cols[0]
                )
                ], style={"margin-left": "15px"})
            ]),
            dbc.Row([
                ### Description
                dcc.Graph(
                    id='desc_table',
                    figure=grf.desc_table,
                    style = {'width':'50%', 'height':'30%'} #
                ),
                dcc.Graph(
                    id='bar_graph',
                    figure=grf.main_graph,
                    style = {'width':'50%', 'height':'30%'} #
                ),
                
            ]),
            
            
             dbc.Row([
                ### Quadruple aim
                html.Div(id='page-content'), 
            ])
        ]),
        
    ]),
    
    
    dbc.Row(dbc.Col(html.Div(html.Hr())))
])

##################################################################################################


main_page = dbc.Container([
      body
], fluid=True)
                
