# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:09:17 2020

@author: Syamanthaka B
"""
import dash
import dash_bootstrap_components as dbc

# meta_tags are required for the app layout to be mobile responsive
"""
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}],
                external_stylesheets=[dbc.themes.BOOTSTRAP])

"""
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.8, '
                                                           'minimum-scale=0.5', }])
server = app.server
app.config.suppress_callback_exceptions = True
