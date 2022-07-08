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
    commonmodules.get_month(),
# adding a header and a paragraph
    html.Div([
                    dbc.Button("This section on the primary healthcare dashboard provides a monthly summary of the "
                               "performance of various indicators as per agreed terms for the various CLCs "
                               "under the CPCS venture.It contains a description of the facility, "
                               "summed values of the indicator numbers and line graphs for each indicator which depict "
                               "the change in performance of the specific indicators since it began being tracked",
                               outline=True, color="secondary"),
                                ],
                            style={'padding':'50px',
                                   'display': 'block',
                                   'size': "15",
                                   'outline': 'True',
                                   'margin-left': 'auto',
                                   'margin-right': 'auto',
                                   'background-position': 'Center',
                                   "font-size": "24px",
                                   'fontWeight':'bold'
                                    }),

],)
##################################################################################################

main_page = dbc.Container([layout],fluid = True)
