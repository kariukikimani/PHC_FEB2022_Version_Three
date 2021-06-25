# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:26:45 2020

@author: Kimani
"""

import dash_html_components as html
import waitress
from flask import Flask

import layouts as lyt
from app import app
from app import server
from waitress import serve
import callbacks
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import data_n_graphs as grf
from dash.dependencies import Input, Output, State
import pandas as pd

csv = "data/annual_data.csv"

# Add global app methods here
def get_database():

    db = pd.read_csv(csv)

    return db
app.title = 'PHC DASHBOARDS'
app.layout = html.Div([
    lyt.main_page
])
###Not in use code section
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/layouts")),
            dbc.DropdownMenu(
                children=[
                    #dbc.DropdownMenuItem("Singapore", href="/home"),
                    html.Div([html.A('Quartely Data', className='tab-button', href='/', target='_blank', style={
                        'color': "light-blue",
                        'family': "Times New Roman, Times, serif",
                    }, )]),
                    html.Div([html.A('Reports', className='tab-button', href='/get_report', target='_blank', style={
                        'color': "light-blue",
                        'family': "Times New Roman, Times, serif",
                    }, )]),
                ],

                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
      #brand="CPCS IMPACT DASHBOARD",
      #  style={
      # 'textAlign': 'center',
      #  },
        color="primary",
        dark=True,
    )
    return navbar


body = html.Div([
    ### Heading Row
    Navbar(),
])
###Code section above not in use

app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=False, port=8050, host='0.0.0.0')
    #waitress.serve(app.wsgifunc, port=8050, url_scheme='https')
    #serve(app, host='0.0.0.0', port=8080)



