import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps import commonmodules,home,MonthlyData,navigation
import dash_bootstrap_components as dbc
from app import app

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_congo(),
    html.H3('Eboteli Data Visualization'),
    dbc.Row(
        [
            dbc.Col(html.Div("One of three columns")),
            dbc.Col(html.Div("One of three columns")),
            dbc.Col(html.Div("One of three columns")),
        ]
    ),
])