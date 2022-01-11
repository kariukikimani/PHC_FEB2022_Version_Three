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
                    dbc.Button("A healthcare dashboard is a modern analytics tool to monitor healthcare KPIs in a "
                               "dynamic and interactive way.A common example is a hospital KPI dashboard, "
                               "that enables healthcare professionals to access important patient statistics "
                               "in real-time to increase the overall hospital performance and patient satisfaction.",
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
