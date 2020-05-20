# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:35:13 2020

@author: Syamanthaka
"""

from dash.dependencies import Input, Output
import dash_html_components as html

from app import app
import data_n_graphs as grf

@app.callback(Output('page-content', 'children'),
              [Input('url', 'hash')])
def display_page(pathname):
    if pathname == '#Aim1':
        return html.Div("About the Aim1")
    elif pathname == '#Aim2':
        return html.Div("About the Aim2")
    elif pathname == '#Aim3':
        return "About the Aim3"
    elif pathname == '#Aim4':
        return "About the Aim4"
    
@app.callback([Output('desc_table', 'figure'),
               Output('bar_graph', 'figure')],
              [Input('facility_select', 'value'),
               Input('y_axis', 'value')])
def facility_updates(facility, y_axis):
    desc_tab = grf.gen_desc_content(facility)
    bar_graph = grf.gen_main_graph(facility, y_axis)
    return desc_tab, bar_graph
    
