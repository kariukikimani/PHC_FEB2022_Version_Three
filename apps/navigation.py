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
# adding a header and a paragraph
    html.Div([

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
    # html.Img(src='assets/Home.jpg',
    # style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'background-position': 'Center',
    # 'width': '50%'}),
    html.Br(),

])

