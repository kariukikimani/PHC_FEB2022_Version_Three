# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:35:57 2020

@author: Syamanthaka B
"""
### Necessary imports
import plotly.graph_objects as go
import pandas as pd
import xml.etree.ElementTree as ET

### Read the main inputs
## Config of graphs
graph_tree = ET.parse('data/monthly_graph_config.xml')
graph_root = graph_tree.getroot()

## Graph data
monthly_df = pd.read_csv('data/monthly_data.csv')
# Extract names of facilities from facility column
# This also becomes a drop down on screen
facility = monthly_df['Facility name'].unique()

## KPI notes data
notes_df = pd.read_excel('data/Kenya KPI dashboard notes.xlsx')

## Config of KPIs
kpi_tree = ET.parse('data/KPI_config.xml')
kpi_root = kpi_tree.getroot()

### Various Functions
## Create dropdown of graphs, from graph config tags
## This is rendered on screen for user to select required graph
def graph_dropdown():
    graph_lst = [x.tag for x in graph_root]
    return graph_lst


graph_lst = graph_dropdown()


## Generate table about description information eg. location, country, description, objectives etc
def gen_desc_content(facility):
    info_df = monthly_df.iloc[:, 0:9]  # First 9 columns contain description info
    info_df_fac = info_df[info_df['Facility name'] == facility]  # Filter for chosen facility

    ### Transpose description information
    desc_df = pd.DataFrame(columns=['Col_name', 'Values'])
    for col in info_df_fac.columns:
        uniq_vals = info_df_fac[col].unique()
        if (len(uniq_vals) == 1):
            the_val = uniq_vals[0]
        elif (len(uniq_vals) > 1):
            the_val = [x + "\n" for x in uniq_vals]
        else:
            the_val = ''
        desc_df = desc_df.append({'Col_name': col, 'Values': the_val}, ignore_index=True)

    # Transposed description table is generated as graph object Table
    info_tab = go.Figure(data=[go.Table(
        header=dict(fill_color='#ccff33', line_color='black', align='center', values=['PROJECT DETAILS', 'DESCRIPTION'],
                    ),
        cells=dict(values=[desc_df['Col_name'], desc_df['Values']],
                   fill_color='white',
                   align='left',
                   font_size=14,
                   font_family="Times New Roman, Times, serif",
                   line_color='black',
                   height=25
                   ))
    ])
    # info_tab.layout['template']['data']['table'][0]['header']['fill']['color']='rgba(0,0,0,0)' #Not displaying header
    info_tab.update_layout(
        margin=dict(l=10, r=10, t=25, b=10),  # Plotly padding reduction
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Times New Roman, Times, serif",
            size=16
        )
    )
    return info_tab


# Calling above function with default option for first time display
desc_table = gen_desc_content(facility[0])


## Function to generate the main graph
def gen_main_graphs(facility, sel_graph):
    # Filter data by selected facility
    fac_filter = monthly_df[monthly_df['Facility name'] == facility]

    # Get details of type of graph etc from graph config
    sel_tag = graph_root.find(sel_graph)

    sel_tag_type = sel_tag.find('type')
    graph_type = sel_tag_type.text

    sel_tag_title = sel_tag.find('title')
    graph_title = sel_tag_title.text

    sel_tag_y = sel_tag.find('y_title')
    y_title = sel_tag_y.text

    main_grf = go.Figure()

    # Single colum graph
    if graph_type == 'bar':
        sel_tag_y = sel_tag.find('col1')
        y_axis = sel_tag_y.text
        main_grf.add_trace(
            go.Bar(x=fac_filter['month'], y=fac_filter[y_axis], marker_color='#008080')
        )

    # Padding and bg color
    main_grf.update_layout(
        margin=dict(l=10, r=10, t=45, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    main_grf.update_layout(
        title=graph_title + ' for ' + facility,
        xaxis_title='month',
        yaxis_title=y_title,
        font=dict(
            family="Times New Roman, Times, serif",
            size=18
        )
    )

    return main_grf


# Calling above function with default option for first time display
main_graph = gen_main_graphs(facility[0], graph_lst[0])


###############################################################


