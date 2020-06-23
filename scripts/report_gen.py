# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:07:10 2020

@author: Syamanthaka
"""
import pandas as pd
import plotly.graph_objects as go
import xml.etree.ElementTree as ET
import generic_functs as gf


### Read the main inputs
## Config of graphs
graph_tree = ET.parse('../data/graph_config.xml')

annual_df = pd.read_csv('../data/annual_data.csv')

graph_root = graph_tree.getroot()

grf_lst = gf.graphs_from_config(graph_root)
facilities = annual_df['Facility name'].unique()

notes_df = pd.read_excel('../data/Kenya KPI dashboard notes.xlsx')

## Config of KPIs
kpi_tree = ET.parse('../data/KPI_config.xml')
kpi_root = kpi_tree.getroot()

aims = ['#Aim1', '#Aim2', '#Aim3', '#Aim4']

graph_html = ''
for facility in facilities:
    info_desc = gf.gen_desc_content(annual_df, facility, 'report')
    graph_html = graph_html + '<h3>' + facility + '</h3><br>' + info_desc
    
    each_aim = ''
    for aim in aims:
        aim_note, visibility, aim_desc = gf.qa_descs(notes_df, aim, facility, 'report')
        kpi_chart = gf.kpi_graphs(annual_df, kpi_root, aim, facility, 'report')
        each_aim = each_aim + '<h4>' + aim + '</h4>' + aim_note + '<br>' + aim_desc + '<br>' + kpi_chart + '<br>'
        
    each_div = ''
    for graph in grf_lst:
        each_grf = gf.gen_main_graph(annual_df, graph_root, facility, graph, 'report')
        each_div = each_div + '<h4>' + graph + '</h4>' + each_grf + '<br>'
    graph_html = graph_html + each_div + each_aim + '<hr>'

beginning = """
    <html>
      <head>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <link rel="stylesheet" href="typography.css">
      </head>
      <body>
          <h1 style={'text-align' : 'center'}, class='nav_bar'>Kenya Community Life Centers: KPIs dashboard</h1>
          <hr>
"""
    
ending = """
    </body>
</html>
"""



report_html = beginning + graph_html + ending

with open("file1.html", "w") as file:
    file.write(report_html)

