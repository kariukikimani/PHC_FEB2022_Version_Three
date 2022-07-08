import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps import commonmodules, home, MonthlyData, navigation
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import data_n_graphs as grf
from apps import MonthlyData, home
from dash.dependencies import Input, Output, State
from app import app
from app import app
import dash
from os import path as os_path

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
meta_tags = [{'name': 'viewport',
              'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]

assets_url_path = '/assets/',
assets_folder = os_path.join(os_path.dirname(os_path.abspath(__file__)), 'assets/')
## Main Home Page
##################################################################################################
# Nav bar items

def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                children=[
                    html.Div([html.A('Home', href='/', target='_blank', style={
                        'textAlign': 'center',
                        'margin-left': '15px',
                        "font-size": "14px",
                        'family': "Times New Roman, Times, serif",
                        'hover': {
                            'color': 'blue'},
                        'visited': {
                            'color': 'green'}
                    }, )]),

                    html.Div([html.A('Reports', href='/get_report', target='_blank', style={
                        'textAlign': 'center',
                        'margin-left': '15px',
                        "font-size": "14px",
                        'family': "Times New Roman, Times, serif",
                        'hover': {
                            'color': 'blue'},
                        'visited': {
                            'color': 'green'}
                    }, )]),
                ],

                nav=True,
                in_navbar=True,
                label="Navigation Menu",
            ),
        ],
        brand="PRIMARY HEALTHCARE DASHBOARD", style={"font-weight": "bold",
                                                      "font-size": "18px",
                                                      'family': "Times New Roman,Times,serif",
                                                      },
        color="Teal",
        dark=True,
    )
    return navbar


body = html.Div([
    ### Heading Row
    Navbar(),

    dbc.Row(dbc.Col(html.Div(html.Hr()))),

    dbc.Row([
        ### Left Column for quadruple aims
        dbc.Col([
            html.Div("Quadruple aims", style={"font-weight": "bold",
                                              "font-size": "20px",
                                              'family': "Times New Roman,Times,serif"}),
            dcc.Location(id='url', refresh=False),








            html.MapEl([
                html.Area(target='', alt='Aim1', title='Improved Patient Experience', href='#Aim1',
                          coords='0,0,125,125', shape='rect',
                          style={"font-weight": "bold",
                                 "font-size": "8px",
                                 'family': "Times New Roman,Times,serif"}),
                html.Area(target='', alt='Aim2', title='Better Health Outcomes', href='#Aim2', coords='125,0,250,125',
                           shape='rect',
                           style={"font-weight": "bold",
                                  "font-size": "8px",
                                  'family': "Times New Roman,Times,serif"}),
                html.Area(target='', alt='Aim3', title='Lower Cost of Care', href='#Aim3', coords='125,125,250,250',
                          shape='rect',
                          style={"font-weight": "bold",
                                 "font-size": "8px",
                                 'family': "Times New Roman,Times,serif"}),
                html.Area(target='', alt='Aim4', title='Improved Staff Experience', href='#Aim4',
                          coords='0,125,125,250', shape='rect',
                          style={"font-weight": "bold",
                                 "font-size": "8px",
                                 'family': "Times New Roman,Times,serif"}),

            ], name='map'),
            html.Img(src='assets/quad_aim4.png', useMap='#map'),

            html.Div(id='qa_generic', className='kpi_text'),
        ], width=4,),

        ### Main column of graphs from annual_data
        dbc.Col([
            dbc.Row([

                ### Facility drop down
                html.Label(["",
                            html.Span("Select Facility From the List:",
                                      style={"font-weight": "bold",
                                             "font-size": "18px",
                                             'family': "Times New Roman,Times,serif"}),
                            dcc.Dropdown(
                                id='facility_select',
                                options=[{'label': i, 'value': i} for i in grf.facility],
                                value=grf.facility[0]
                            )
                            ], style={
                                        'textAlign': 'center',
                                        'margin-left': '15px',
                                        "font-size": "14px",
                                        'family': "Times New Roman, Times, serif"
                                    }),

                html.Label(["",
                            html.Span("Select Analysis Graph to Display:",
                                      style={"font-weight": "bold",
                                             "font-size": "18px",
                                             'family': "Times New Roman,Times,serif"}),
                            dcc.Dropdown(
                                id='graph_id',
                                options=[{'label': i, 'value': i} for i in grf.graph_lst],
                                value=grf.graph_lst[0]
                            )
                            ], style={
                                        'textAlign': 'center',
                                        'margin-left': '15px',
                                        "font-size": "14px",
                                        'family': "Times New Roman, Times, serif",

                })
                # style={"margin-left": "15px"})

            ]),
            dbc.Row([
                ### Description
                dcc.Graph(
                    id='desc_table',
                    figure=grf.desc_table,
                    style={'width': '70%', 'height': '50%',
                           'color': 'black',
                           'if': {'row_index': 'odd'} , 'backgroundColor': 'white',
                           'fontWeight': 'bold'
                           },
                ),

                dcc.Graph(
                    id='bar_graph',
                    figure=grf.main_graph,
                    style={'width': '94%', 'height': '30%'}  #
                ),

            ],),

            dbc.Row([
                ### Quadruple aim
                dbc.Col([
                    html.Div(id='kpi-content',
                             style={'visibility': 'hidden'},
                             children=[
                                 dcc.Graph(
                                     id='kpi_table',
                                     figure=grf.kpi_table,
                                     style={'width': '100%', 'height': '100%'}  #
                                 ),
                             ])
                ]),
                dbc.Col([
                    html.Div(id='kpi-content2',
                             style={'visibility': 'hidden'},
                             children=[
                                 dcc.Graph(
                                     id='kpi_chart',
                                     figure=grf.kpi_chart,
                                     style={'width': '100%', 'height': '100%'}
                                 )
                             ]
                             )
                ]),

            ])
        ]),

    ]),

    dbc.Row(dbc.Col(html.Div(html.Hr())))
])
##################################################################################################

main_page = dbc.Container([body], fluid=True)
