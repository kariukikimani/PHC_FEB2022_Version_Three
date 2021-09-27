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
        color="primary",
        dark=True,
    )
    return navbar

def yearly():
    year = dbc.NavbarSimple(
        children=[

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
        color="primary",
        dark=True,
    )
    return year

def get_menu():
    menu = html.Div([

        dcc.Link('Home', href='/', className="p-2 text-dark", style={"font-weight": "bold",
                                                                     "font-size": "18px",
                                                                     'family': "Times New Roman,Times,serif",
                                                                     'hover': {'color': 'blue'},
                                                                     'visited': {'color': 'green'}
                                                                     },),
        dcc.Link('Monthly Data   ', href='/MonthlyData', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                           "font-size": "18px",
                                                                                           'family': "Times New Roman,Times,serif",
                                                                                           'hover': {'color': 'blue'},
                                                                                           'visited': {'color': 'green'}
                                                                                           },),
        dcc.Link('Yearly Data   ', href='/home', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                   "font-size": "18px",
                                                                                   'family': "Times New Roman,Times,serif",
                                                                                   'hover': {
                                                                                       'color': 'blue'},
                                                                                   'visited': {
                                                                                       'color': 'green'}
                                                                                   },),
        dcc.Link('Congo Data   ', href='/Eboteli', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                     "font-size": "18px",
                                                                                     'family': "Times New Roman,Times,serif",
                                                                                     'hover': {
                                                                                         'color': 'blue'},
                                                                                     'visited': {
                                                                                         'color': 'green'}
                                                                                     },),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_kenyamonth():
    menu = html.Div([

        dcc.Link('Home   ', href='/MonthlyData', className="p-2 text-dark", style={"font-weight": "bold",
                                                                        "font-size": "18px",
                                                                        'family': "Times New Roman,Times,serif",
                                                                        'hover': {
                                                                                   'color': 'blue'},
                                                                        'visited': {
                                                                                    'color': 'green'}
                                                                                   }, ),
        dcc.Link('Matiku Monthly Data   ', href='/Matiku', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif",
                                                                                             'hover': {
                                                                                                 'color': 'blue'},
                                                                                             'visited': {
                                                                                                 'color': 'green'}
                                                                                             }, ),
        dcc.Link('Tutini Monthly Data   ', href='/Tutini', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif",
                                                                                             'hover': {
                                                                                                 'color': 'blue'},
                                                                                             'visited': {
                                                                                                 'color': 'green'}
                                                                                             }, ),
        dcc.Link('Dandu Monthly Data   ', href='/Dandu', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                           "font-size": "18px",
                                                                                           'family': "Times New Roman,Times,serif",
                                                                                           'hover': {
                                                                                               'color': 'blue'},
                                                                                           'visited': {
                                                                                               'color': 'green'}
                                                                                           }, ),
        dcc.Link('Githurai Monthly Data   ', href='/Githurai', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                                 "font-size": "18px",
                                                                                                 'family': "Times New Roman,Times,serif",
                                                                                                 'hover': {
                                                                                                     'color': 'blue'},
                                                                                                 'visited': {
                                                                                                     'color': 'green'}
                                                                                                 }, ),
        dcc.Link('Emali Monthly Data   ', href='/Emali', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                           "font-size": "18px",
                                                                                           'family': "Times New Roman,Times,serif",
                                                                                           'hover': {
                                                                                               'color': 'blue'},
                                                                                           'visited': {
                                                                                               'color': 'green'}
                                                                                           }, ),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_SA_Month():
    menu = html.Div([

        dcc.Link('Home   ', href='/MonthlyData', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                       'family': "Times New Roman,Times,serif",
                                                                       'hover': {
                                                                                  'color': 'blue'},
                                                                        'visited': {
                                                                                   'color': 'green'}
                                                                                  },),
        dcc.Link('Diepsloot Monthly Data  ', href='/Diepsloot', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif",
                                                                                              'hover': {
                                                                                                        'color': 'blue'},
                                                                                              'visited': {
                                                                                                        'color': 'green'}
                                                                                                  },),
        dcc.Link('OrangeFarm Monthly Data   ', href='/OrangeFarm', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif",
                                                                                                     },),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_month():
    menu = html.Div([

        dcc.Link('Home   ', href='/', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                       'family': "Times New Roman,Times,serif", },),
        dcc.Link('Kenya Sites   ', href='/Kenya_CLC_Sites', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif", },),
        dcc.Link('SouthAfrica Sites   ', href='/SouthAfrica_CLC_Sites', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif", },),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_diepsloot_menu():
    menu = html.Div([

        dcc.Link('Home', href='/SouthAfrica_CLC_Sites', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                       'family': "Times New Roman,Times,serif", },),
        dcc.Link('OrangeFarm Monthly Data', href='/OrangeFarm', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif", },),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu
def get_orangefarm_menu():
    menu = html.Div([

        dcc.Link('Home', href='/SouthAfrica_CLC_Sites', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                       'family': "Times New Roman,Times,serif", },),
        dcc.Link('Diepsloot Monthly Data   ', href='/Diepsloot', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif", },),
    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_dandu_menu():
    menu = html.Div([

        dcc.Link('Home   ', href='/Kenya_CLC_Sites', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                       'family': "Times New Roman,Times,serif", },),
        dcc.Link('Matiku Monthly Data   ', href='/Matiku', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif", },),
        dcc.Link('Emali Monthly Data   ', href='/Emali', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                           "font-size": "18px",
                                                                                           'family': "Times New Roman,Times,serif", },),
        dcc.Link('Githurai Monthly Data   ', href='/Githurai', className="p-2 text-dark",style={"font-weight": "bold",
                                                                                                "font-size": "18px",
                                                                                                'family': "Times New Roman,Times,serif", }, ),
        dcc.Link('Tutini Monthly Data   ', href='/Tutini', className="p-2 text-dark",style={"font-weight": "bold",
                                                                                            "font-size": "18px",
                                                                                            'family': "Times New Roman,Times,serif", }, ),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_matiku_menu():
    menu = html.Div([

        dcc.Link('Home', href='/Kenya_CLC_Sites', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                       'family': "Times New Roman,Times,serif", },),
        dcc.Link('Dandu Monthly Data   ', href='/Dandu', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                           "font-size": "18px",
                                                                                           'family': "Times New Roman,Times,serif", },),
        dcc.Link('Emali Monthly Data   ', href='/Emali', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                           "font-size": "18px",
                                                                                           'family': "Times New Roman,Times,serif", },),
        dcc.Link('Githurai Monthly Data   ', href='/Githurai', className="p-2 text-dark",style={"font-weight": "bold",
                                                                                                "font-size": "18px",
                                                                                                'family': "Times New Roman,Times,serif", }, ),
        dcc.Link('Tutini Monthly Data   ', href='/Tutini', className="p-2 text-dark",style={"font-weight": "bold",
                                                                                            "font-size": "18px",
                                                                                            'family': "Times New Roman,Times,serif", }, ),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_emali_menu():
    menu = html.Div([

        dcc.Link('Home', href='/Kenya_CLC_Sites', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                       'family': "Times New Roman,Times,serif", },),
        dcc.Link('Dandu Monthly Data   ', href='/Dandu', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                           "font-size": "18px",
                                                                                           'family': "Times New Roman,Times,serif", },),
        dcc.Link('Matiku Monthly Data   ', href='/Matiku', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family': "Times New Roman,Times,serif", },),
        dcc.Link('Githurai Monthly Data   ', href='/Githurai', className="p-2 text-dark",style={"font-weight": "bold",
                                                                                                "font-size": "18px",
                                                                                                'family': "Times New Roman,Times,serif", }, ),
        dcc.Link('Tutini Monthly Data   ', href='/Tutini', className="p-2 text-dark",style={"font-weight": "bold",
                                                                                            "font-size": "18px",
                                                                                            'family': "Times New Roman,Times,serif", }, ),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_githurai_menu():
    menu = html.Div([

        dcc.Link('Home', href='/Kenya_CLC_Sites', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                       'family': "Times New Roman,Times,serif", },),
        dcc.Link('Dandu Monthly Data   ', href='/Dandu', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                           "font-size": "18px",
                                                                                           'family': "Times New Roman,Times,serif", },),
        dcc.Link('Matiku Monthly Data   ', href='/Matiku', className="p-2 text-dark", style={"font-weight": "bold",
                                                                                             "font-size": "18px",
                                                                                             'family':
                                                                                             "Times New Roman,Times,serif",},),
        dcc.Link('Emali Monthly Data   ', href='/Emali', className="p-2 text-dark",style={"font-weight": "bold",
                                                                                          "font-size": "18px",
                                                                                          'family':
                                                                                          "Times New Roman,Times,serif",},),
        dcc.Link('Tutini Monthly Data   ', href='/Tutini', className="p-2 text-dark",style={"font-weight": "bold", "font-size": "18px", 'family': "Times New Roman,Times,serif", }, ),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_tutini_menu():
    menu = html.Div([

        dcc.Link('Home',href='/Kenya_CLC_Sites', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                       'family': "Times New Roman,Times,serif", },),
        dcc.Link('Dandu Monthly Data   ', href='/Dandu', className="p-2 text-dark", style={"font-weight": "bold", "font-size": "18px", 'family': "Times New Roman,Times,serif", },),
        dcc.Link('Matiku Monthly Data   ', href='/Matiku', className="p-2 text-dark", style={"font-weight": "bold", "font-size": "18px", 'family': "Times New Roman,Times,serif", },),
        dcc.Link('Emali Monthly Data   ', href='/Emali', className="p-2 text-dark",style={"font-weight": "bold", "font-size": "18px", 'family': "Times New Roman,Times,serif", }, ),
        dcc.Link('Githurai Monthly Data   ', href='/Githurai', className="p-2 text-dark",style={"font-weight": "bold", "font-size": "18px", 'family': "Times New Roman,Times,serif", }, ),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu

def get_congo():
    menu = html.Div([

        dcc.Link('Home   ', href='/', className="p-2 text-dark",style={"font-weight": "bold",
                                                                       "font-size": "18px",
                                                                        'family': "Times New Roman,Times,serif", },),
        dcc.Link('Monthly Data   ', href='/MonthlyData', className="p-2 text-dark",
                 style={"font-weight": "bold", "font-size": "18px", 'family': "Times New Roman,Times,serif", }, ),
        dcc.Link('Yearly Data   ', href='/home', className="p-2 text-dark", style={"font-weight": "bold", "font-size": "18px", 'family': "Times New Roman,Times,serif", },),

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