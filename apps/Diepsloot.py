import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from apps import commonmodules,home,MonthlyData,navigation
import data_m_graphs as grp
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app
import dash
import plotly.graph_objects as go
from plotly.subplots import make_subplots

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}
card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("IMMUNIZATION TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("28,756", id="card-value",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "12px",
                           'family': "Times New Roman,Times,serif", "color": "blue", }),
        ]
    )
)
card1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("FP TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("5,830", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                   'family': "Times New Roman,Times,serif", "color": "blue",}),
        ]
    )
)
card2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("CURATIVE TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("1,116", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                   'family': "Times New Roman,Times,serif","color": "blue", }),
        ]
    )
)
card3 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("ANC TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("1,879", id="card-value", style={"font-weight": "bold", "text-align": "center", "font-size": "12px",
                                                     'family': "Times New Roman,Times,serif", "color": "blue", }),
        ]
    )
)
card4 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("NUMBER OF LIVES IMPROVED", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("0", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                   'family': "Times New Roman,Times,serif","color": "blue", }),
        ]
    )
)
# Our dataframe
df = pd.read_csv('data/Diepsloot_Data.csv')
df1 = pd.read_csv('data/Diepsloot_Facility_Information_Data.csv')

fig = px.scatter(df, x='Year', y='ImmunizationClientsSeenPerMonth')
fig.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig.layout.plot_bgcolor = '#FFFFFF'
fig.layout.paper_bgcolor = '#fff'
fig.update_xaxes(showgrid=False)
fig.update_yaxes(range=(0, 1000))

fig1 = px.scatter(df, x='Year', y='FPClientsSeenPerMonth')
fig1.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig1.layout.plot_bgcolor = '#FFFFFF'
fig1.layout.paper_bgcolor = '#fff'
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(range=(0, 500))

fig2 = px.scatter(df, x='Year', y='CurativeClientsSeenPerMonth')
fig2.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig2.layout.plot_bgcolor = '#FFFFFF'
fig2.layout.paper_bgcolor = '#fff'
fig2.update_xaxes(showgrid=False)
fig2.update_yaxes(range=(0 ,200))

fig3 = px.scatter(df, x='Year', y='ANCClientsSeenPerMonth')
fig3.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig3.layout.plot_bgcolor = '#FFFFFF'
fig3.layout.paper_bgcolor = '#fff'
fig3.update_xaxes(showgrid=False)
fig3.update_yaxes(range=(0 , 200))

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_diepsloot_menu(),
    html.H3('DIEPSLOOT MONTHLY DATA VISUALIZATION',
            style={"font-weight": "bold", "text-align": "center", "font-size": "18px",
                   'family': "Times New Roman,Times,serif", }),
    html.Div([dash_table.DataTable(

                            id='Desc',
                            columns=[{"Facility name": i, "id": i} for i in df1.columns],
                            data=df1.to_dict('records'),
                            style_table={'Height': 200, 'Width': 100, 'overflowX': 'auto'},
                            style_header={
                                'backgroundColor': 'Teal',
                                'fontWeight': 'bold',
                                'font-family': "Times New Roman,Times,serif",
                            },
                            style_cell={'textAlign': 'Center',  'overflow': 'hidden',
                                         'fontSize': 12,
                                        'textOverflow': 'ellipsis',
                                        # all three widths are needed
                                        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                        'whiteSpace': 'normal',
                                        'background': 'white',
                                        'padding': '10px',
                                        'font-family': "Times New Roman,Times,serif",

                                        },

                            style_data={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                        'lineHeight': '15px',
                                        'fontSize': 12,
                                        'textOverflow': 'ellipsis',
                                        'padding': '5px',
                                        'font-family': "Times New Roman,Times,serif",

                                    },
                        ),]),
    html.Div(
        [html.Label(["INDICATORS SUMMARY"],
                    style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                           'family': "Times New Roman,Times,serif", }),]),
        dbc.Row([
        dbc.Col([card]), dbc.Col([card1]), dbc.Col([card2]), dbc.Col([card3]), dbc.Col([card4])
               ]),
    html.Div(
        [html.Label(["IMMUNIZATION MONTHLY PERFORMANCE"],
                    style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                           'family': "Times New Roman,Times,serif", }),
             dcc.Graph(
             id='Immunization-graph',
             figure=fig
    ),]),

    html.Label(["FAMILY PLANNING CLINIC MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='fp-graph',
        figure=fig1
    ),
    html.Label(["CURATIVE CARE CLINIC  MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='Curative-graph',
        figure=fig2
    ),
    html.Label(["ANTENATAL CARE CLINIC  MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='ANC-graph',
        figure=fig3
    ),

]),


##################################################################################################

main_page = dbc.Container([layout],fluid = True)
