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

app.title='CPCS IMPACT DASHBOARD'
app.layout = html.Div([
    lyt.main_page
])

app.config.suppress_callback_exceptions = True
#app = Flask(__name__)

if __name__ == '__main__':
    app.run_server(debug='False', port=8050, host='0.0.0.0')
    #waitress.serve(app.wsgifunc, port=8050, url_scheme='https')
    #serve(app, host='0.0.0.0', port=8080)



