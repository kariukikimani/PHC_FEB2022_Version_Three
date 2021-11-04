import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from os import path as os_path

assets_url_path = '/assets/',
assets_folder = os_path.join(os_path.dirname(os_path.abspath(__file__)), 'assets/')

def get_header():
    navbar = dbc.NavbarSimple(
        brand="PRIMARY HEALTHCARE DASHBOARD HOME", style={"font-weight": "bold",
                                                           "font-size": "18px",
                                                           'family': "Times New Roman,Times,serif"},
        color="Teal",
        dark=True,
    )
    return navbar
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
def yearly():
    year = dbc.NavbarSimple(
        children=[
            dbc.Button('Home', href='/', color="light", className="me-1", style={"font-size": "18px"}, ),
            dbc.Button('Reports', href='/get_report', color="light", className="me-1", style={"font-size": "18px"}, ),

            dcc.Link('Home', href='/', className="p-2 text-dark", style={"font-weight": "bold",
                                                                         "font-size": "18px",
                                                                         'family': "Times New Roman,Times,serif",
                                                                         'hover': {'color': 'blue'},
                                                                         'visited': {'color': 'green'}
                                                                         }, ),
            dcc.Link('Reports', href='/get_report', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                               "font-size": "18px",
                                                                                               'family': "Times New Roman,Times,serif",
                                                                                               'hover': {
                                                                                                   'color': 'blue'},
                                                                                               'visited': {
                                                                                                   'color': 'green'}
                                                                                               }, ),

       ###Add dropdown menu
        ],
        brand="PRIMARY HEALTHCARE DASHBOARDS", style={"font-weight": "bold",
                                                      "font-size": "18px",
                                                      'family': "Times New Roman,Times,serif",
                                                      },
        color="Teal",
        dark=True,
    )
    return year

def get_menu():
    menu = html.Div([
        dbc.Button('Monthly Data', href='/MonthlyData', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button('Yearly Data', href='/home', color="light", className="me-1",style={"font-size": "18px"}, ),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_kenyamonth():
    menu = html.Div([
        dbc.Button('Home', href='/MonthlyData', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button('Matiku Monthly Data', href='/Matiku', color="light", className="me-1",style={"font-size": "18px"},),
        dbc.Button('Tutini Monthly Data', href='/Tutini', color="light", className="me-1",style={"font-size": "18px"},),
        dbc.Button('Dandu Monthly Data',  href='/Dandu', color="light", className="me-1", style={"font-size": "18px"},),
        dbc.Button('Githurai Monthly Data', href='/Githurai', color="light", className="me-1",style={"font-size": "18px"},),
        dbc.Button('Emali Monthly Data', href='/Emali', color="light", className="me-1",style={"font-size": "18px"}, ),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_SA_Month():
    menu = html.Div([
        dbc.Button("Home", href='/MonthlyData', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button('Diepsloot Monthly Data', href='/Diepsloot', color="light", className="me-1",style={"font-size": "18px"}, ),
        dbc.Button('OrangeFarm Monthly Data', href='/OrangeFarm', color="light", className="me-1",style={"font-size": "18px"}, ),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_month():
    menu = html.Div([
        dbc.Button("Home", href='/', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Kenya Sites", href='/Kenya_CLC_Sites', color="light", className="me-1",style={"font-size": "18px"}, ),
        dbc.Button('SouthAfrica Sites', href='/SouthAfrica_CLC_Sites', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button('Congo Site', href='/Eboteli', color="light", className="me-1",style={"font-size": "18px"}, ),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_diepsloot_menu():
    menu = html.Div([
        dbc.Button("Home", href='/SouthAfrica_CLC_Sites', color="light", className="me-1",style={"font-size": "18px"}, ),
        dbc.Button('OrangeFarm Monthly Data', href='/OrangeFarm', color="light", className="me-1",style={"font-size": "18px"}, ),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu
def get_orangefarm_menu():
    menu = html.Div([

        dbc.Button("Home", href='/SouthAfrica_CLC_Sites', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button('Diepsloot Monthly Data', href='/Diepsloot', color="light", className="me-1",
                   style={"font-size": "18px"}, ),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_dandu_menu():
    menu = html.Div([

        dbc.Button("Home", href='/Kenya_CLC_Sites', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Matiku Monthly Data", href='/Matiku', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Emali Monthly Data", href='/Emali', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Githurai Monthly Data", href='/Githurai', color="light", className="me-1",style={"font-size": "18px"}, ),
        dbc.Button("Tutini Monthly Data", href='/Tutini', color="light", className="me-1",style={"font-size": "18px"}, ),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_matiku_menu():
    menu = html.Div([

        dbc.Button("Home", href='/Kenya_CLC_Sites', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Dandu Monthly Data", href='/Dandu', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Emali Monthly Data", href='/Emali', color="light", className="me-1",style={"font-size": "18px"}, ),
        dbc.Button("Githurai Monthly Data", href='/Githurai', color="light", className="me-1",style={"font-size": "18px"}, ),
        dbc.Button("Tutini Monthly Data", href='/Tutini', color="light", className="me-1",style={"font-size": "18px"}, ),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_emali_menu():

    menu = html.Div([
        dbc.Button("Home", href='/Kenya_CLC_Sites', color="light", className="me-1",style={"font-size": "18px"},),
        dbc.Button("Dandu Monthly Data", href='/Dandu', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Matiku Monthly Data", href='/Matiku', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Githurai Monthly Data", href='/Githurai', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Tutini Monthly Data", href='/Tutini', color="light", className="me-1", style={"font-size": "18px"}, ),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_githurai_menu():
    menu = html.Div([

        dbc.Button("Home", href='/Kenya_CLC_Sites', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Dandu Monthly Data", href='/Dandu', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Matiku Monthly Data", href='/Matiku', color="light", className="me-1",style={"font-size": "18px"}, ),
        dbc.Button("Emali Monthly Data", href='/Emali', color="light", className="me-1",style={"font-size": "18px"},),
        dbc.Button("Tutini Monthly Data", href='/Tutini', color="light", className="me-1",style={"font-size": "18px"}, ),

         ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_tutini_menu():
    menu = html.Div([

        dbc.Button("Home", href='/Kenya_CLC_Sites', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Dandu Monthly Data", href='/Dandu', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Matiku Monthly Data", href='/Matiku', color="light", className="me-1",style={"font-size": "18px"}, ),
        dbc.Button("Emali Monthly Data", href='/Emali', color="light", className="me-1", style={"font-size": "18px"}, ),
        dbc.Button("Githurai Monthly Data", href='/Githurai', color="light", className="me-1",style={"font-size": "18px"}, ),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_congo():
    menu = html.Div([
        dbc.Button('Home', href='/MonthlyData', color="light", className="me-1", style={"font-size": "18px"}, ),
           ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def navbar_monthly():
 navbar_sales = html.Div([

        html.Div([], className = 'col-3'),

        html.Div([
            dcc.Link(
                html.H4(children = 'Sales Overview',
                        style = {"font-weight": "bold", "font-size": "18px", 'family': "Times New Roman,Times,serif", },),
                href='/apps/sales-overview'
                )
        ],
        className='col-2'),

        html.Div([
            dcc.Link(
                html.H4(children = 'Page 2'),
                href='/apps/page2'
                )
        ],
        className='col-2'),

        html.Div([
            dcc.Link(
                html.H4(children = 'Page 3'),
                href='/apps/page3'
                )
        ],
        className='col-2'),

        html.Div([], className = 'col-3')

    ],
    className = 'row',
    style = {'background-color' : 'white',
            'box-shadow': '2px 5px 5px 1px rgba(255, 101, 131, .5)'}
    )