# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:35:57 2020

@author: Syamanthaka B
"""
import plotly.graph_objects as go
import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse('data/graph_config.xml')
root = tree.getroot()

annual_df = pd.read_csv('data/annual_data.csv')
facility = annual_df['Facility name'].unique()

notes_df = pd.read_excel('data/Kenya KPI dashboard notes.xlsx')

def graph_dropdown():
    graph_lst = [x.tag for x in root]
    return graph_lst
graph_lst = graph_dropdown()

def gen_desc_content(facility):
    info_df = annual_df.iloc[:,0:9]
    info_df_fac = info_df[info_df['Facility name'] == facility]
    
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
        desc_df = desc_df.append({'Col_name' : col, 'Values' : the_val}, ignore_index=True)
    
     
    info_tab = go.Figure(data=[go.Table(
         header=dict(fill_color='white', line_color='black'),
        cells=dict(values=[desc_df['Col_name'], desc_df['Values']],
                   fill_color='white',
                   align='left',
                   font_size=14,
                   line_color='black',
                   ))#height=30
            ])
    # info_tab.layout['template']['data']['table'][0]['header']['fill']['color']='rgba(0,0,0,0)' #Not displaying header
    info_tab.update_layout(
        margin=dict(l=10, r=10, t=25, b=10), #Plotly padding reduction
    )
    

    return info_tab
desc_table = gen_desc_content(facility[0])


def gen_main_graph(facility, sel_graph):
    fac_filter = annual_df[annual_df['Facility name'] == facility]
    
    sel_tag = root.find(sel_graph)
    
    sel_tag_type = sel_tag.find('type')
    graph_type = sel_tag_type.text
    
    sel_tag_title = sel_tag.find('title')
    graph_title = sel_tag_title.text
    
    sel_tag_y = sel_tag.find('y_title')
    y_title = sel_tag_y.text
    
    main_grf = go.Figure()
    
    if graph_type == 'bar':
        sel_tag_y = sel_tag.find('col1')
        y_axis = sel_tag_y.text
        main_grf.add_trace(
            go.Bar(x=fac_filter['Year'], y=fac_filter[y_axis])
        )
    else:
        sel_tag_col1 = sel_tag.find('col1')
        y1 = sel_tag_col1.text
        sel_tag_col2 = sel_tag.find('col2')
        y2 = sel_tag_col2.text
        main_grf.add_trace(
            go.Bar(x=fac_filter['Year'], y=fac_filter[y1], name=y1)
        )
        if graph_type == 'bar-bar':
            main_grf.add_trace(
                go.Bar(x=fac_filter['Year'], y=fac_filter[y2], name=y2)
            )
        else:
            main_grf.add_trace(
                go.Scatter(x=fac_filter['Year'], y=fac_filter[y2], name=y2)
            )
        
    
    main_grf.update_layout(
        margin=dict(l=10, r=10, t=25, b=10),
    )
    main_grf.update_layout(
        title= graph_title + ' for ' + facility,
        xaxis_title='Year',
        yaxis_title=y_title)
    
    return main_grf
main_graph = gen_main_graph(facility[0], graph_lst[0])


###############################################################
### KPI Section

def qa_descs(sel_aim, facility):
    selected_aim = sel_aim.split('#')[1]
    
    
    facility_df = notes_df[notes_df['Facility'] == facility]
    facility_aim_df = facility_df[facility_df['Quadruple Aim'] == selected_aim]
    
    try:
        generic_kpi_note = facility_aim_df['KPI'].unique()[0]
    except IndexError:
        return 'No information available', {'visibility':'hidden'}, go.Figure()

    
    facility_kpi_table = facility_aim_df.iloc[:, 3:6]
    kpi_table = go.Figure(data=[go.Table(
        header=dict(values=['Indicator', 'Indicator description', 'Results'],
                    line_color='black',
                    fill_color='lightgrey'),
        cells=dict(values=[facility_kpi_table['Indicator'], facility_kpi_table['Indicator description'], facility_kpi_table['Results']],
                   fill_color='white',
                   align='left',
                   font_size=14,
                   line_color='black',
                   ))#height=30
            ])
   
    kpi_table.update_layout(
        margin=dict(l=10, r=10, t=25, b=10), #Plotly padding reduction
    )
    return generic_kpi_note, {'visibility':'visible'}, kpi_table
   
kpi_table = go.Figure()
