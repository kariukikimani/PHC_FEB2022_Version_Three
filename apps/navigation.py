import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps import home,MonthlyData,navigation, commonmodules
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import data_n_graphs as grf

from app import app
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


layout = html.Div([


    commonmodules.get_header(),
    commonmodules.get_menu(),
    html.Br(),
])

