# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:26:45 2020

@author: Kimani
"""

import dash_html_components as html
import waitress
from dash import dash
from flask import Flask
# Connect to main app.py file
from app import app
from app import server
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
from apps import MonthlyData, home, navigation

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from apps import MonthlyData, home, navigation, Eboteli, Dandu, Matiku, Githurai, Tutini, Emali, Kenya_CLC_Sites, SouthAfrica_CLC_Sites,Diepsloot,OrangeFarm

app.title = 'PHC DASHBOARDS'
app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return navigation.layout
    elif pathname == '/home':
         return  home.body
    elif pathname == '/MonthlyData':
        return MonthlyData.layout
    elif pathname == '/Eboteli':
        return Eboteli.layout
    elif pathname == '/Dandu':
        return Dandu.layout
    elif pathname == '/Matiku':
        return Matiku.layout
    elif pathname == '/Tutini':
        return Tutini.layout
    elif pathname == '/Emali':
        return Emali.layout
    elif pathname == '/Githurai':
        return Githurai.layout
    elif pathname == '/Kenya_CLC_Sites':
        return Kenya_CLC_Sites.layout
    elif pathname == '/SouthAfrica_CLC_Sites':
        return SouthAfrica_CLC_Sites.layout
    elif pathname == '/Diepsloot':
        return Diepsloot.layout
    elif pathname == '/OrangeFarm':
        return OrangeFarm.layout
    else:
        return '404'

external_css = ["hhttps://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]


if __name__ == '__main__':
    app.run_server(debug=False, port=8050, host='0.0.0.0')
    #waitress.serve(app.wsgifunc, port=8050, ssl_context='adhoc',url_scheme='https')
    #serve(app, host='0.0.0.0', port=8080)



