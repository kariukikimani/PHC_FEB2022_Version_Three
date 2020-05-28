# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:35:13 2020

@author: Syamanthaka
"""

from dash.dependencies import Input, Output
import dash_html_components as html

from app import app
import data_n_graphs as grf

@app.callback([Output('qa_generic', 'children'), 
               Output('kpi-content', 'style'),
               Output('kpi_table', 'figure')],
              [Input('url', 'hash'),
               Input('facility_select', 'value')])
def display_page(pathname, facility):
    generic_notes, kpi_content_style, facility_kpi_table = grf.qa_descs(pathname, facility)
    return generic_notes, kpi_content_style, facility_kpi_table
    
    
@app.callback([Output('desc_table', 'figure'),
               Output('bar_graph', 'figure')],
              [Input('facility_select', 'value'),
               Input('graph_id', 'value')])
def facility_updates(facility, graph_id):
    desc_tab = grf.gen_desc_content(facility)
    bar_graph = grf.gen_main_graph(facility, graph_id)
    return desc_tab, bar_graph
    
