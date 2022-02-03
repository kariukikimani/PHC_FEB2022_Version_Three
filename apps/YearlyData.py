import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps import commonmodules,home,MonthlyData,navigation
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_yearmenu(),
# adding a header and a paragraph
    html.Div([
                    dbc.Button("This section on the primary healthcare dashboard provides the yearly summary of the "
                               "performance of various indicators as per agreed terms for the various CLCs under the CPCS venture."
                               "It contains a description of the facility and the details of the project inception,"
                               "A circular custom select menu with labels of the various quadruple aims in each quadrangle,"
                               "two drop down lists for facility selection and graph selection as well as an Indicator performance "
                               "explanation table which updates on selection of a specific quadruple aim and shows the "
                               "indicator numbers from when the indicator began to be tracked, to the present year and "
                               "the percentage change.Lastly one is able to download a report of the yearly data which contains description information for each "
                               "of the clc sites as well as the indicator performance and explanation.Which can be saved as a html file or pdf.",
                               outline=True, color="secondary"),
                                ],
                            style={'padding':'50px',
                                   'display': 'block',
                                   'size': "md",
                                   'outline': 'True',
                                   'margin-left': 'auto',
                                   'margin-right': 'auto',
                                   'background-position': 'Center',
                                   "font-size": "24px"
                                    }),

],)
##################################################################################################

main_page = dbc.Container([layout],fluid = True)
