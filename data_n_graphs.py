# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:35:57 2020

@author: Syamanthaka B
"""
import plotly.graph_objects as go
import pandas as pd


annual_df = pd.read_csv('data/annual_data.csv')
facility = annual_df['Facility name'].unique()
#
y_cols = list(annual_df.columns[10:])

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
        # header=dict(style_header = {'display': 'none'}),
        cells=dict(values=[desc_df['Col_name'], desc_df['Values']],
                   fill_color='white',
                   align='left',
                   font_size=14,
                   line_color='black',
                   ))#height=30
            ])
    info_tab.layout['template']['data']['table'][0]['header']['fill']['color']='rgba(0,0,0,0)' #Not displaying header
    info_tab.update_layout(
        margin=dict(l=10, r=10, t=25, b=10), #Plotly padding reduction
    )
    

    return info_tab
desc_table = gen_desc_content(facility[0])


def gen_main_graph(facility, y_axis):
    fac_filter = annual_df[annual_df['Facility name'] == facility]
    
    main_grf = go.Figure()
    main_grf.add_trace(
        go.Bar(name='Test', x=fac_filter['Year'], y=fac_filter[y_axis])
    )
    main_grf.update_layout(
        margin=dict(l=10, r=10, t=25, b=10),
    )
    main_grf.update_layout(
        title='Number of ' + y_axis + ' per year for ' + facility,
        xaxis_title='Year',
        yaxis_title=y_axis)
    
    return main_grf
main_graph = gen_main_graph(facility[0], y_cols[0])