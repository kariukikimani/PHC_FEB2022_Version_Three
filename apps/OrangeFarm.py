import pathlib

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
            html.H4("IMMUNIZATIONS DONE SINCE JAN-2019", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "10px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("3692", id="card-value",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "25px",
                           'family': "Times New Roman,Times,serif", "color": "#23282D", }),
        ]
    )
)
card1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("FP PATIENTS SEEN SINCE JAN-2019", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "10px",
                           'family': "Times New Roman,Times,serif", }),


            html.H2("808", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "25px",
                                                   'family': "Times New Roman,Times,serif", "color": "#23282D"}),

        ]
    )
)
card2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("CURATIVE PATIENTS SEEN SINCE JAN-2019", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "10px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("1026", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "25px",
                                                   'family': "Times New Roman,Times,serif","color": "#23282D"}),
        ]
    )
)
card3 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("ANC PATIENTS SEEN SINCE JAN-2019", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "10px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("152", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "25px",
                                                   'family': "Times New Roman,Times,serif","color": "#23282D"}),
        ]
    )
)
card4 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("LIVES IMPROVED SINCE JAN-2019", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "10px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("5678", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "25px",
                                                   'family': "Times New Roman,Times,serif","color": "#23282D"}),
        ]
    )
)
PATH = pathlib.Path(__file__) .parent
DATA_PATH = PATH.joinpath("../data").resolve()
df2 = pd.read_csv(DATA_PATH.joinpath("Orangefarm_Card.csv"))

# Our dataframe
# Get Relative Data Folder
PATH = pathlib.Path(__file__) .parent
DATA_PATH = PATH.joinpath("../data").resolve()
df = pd.read_csv(DATA_PATH.joinpath("OrangeFarm_Data.csv"))
df1 = pd.read_csv(DATA_PATH.joinpath("OrangeFarm_Facility_Information_Data.csv"))

fig = px.scatter(df, x='Year', y='ImmunizationClientsSeenPerMonth')
fig.update_layout(title="IMMUNIZATION MONTHLY PERFORMANCE FOR ORANGEFARM",
                  font=dict(
                      family="Times New Roman,Times,serif",
                      size=13,
                      color="#231F20",
                  ))
fig.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig.layout.plot_bgcolor = '#FFFFFF'
fig.layout.paper_bgcolor = '#fff'
fig.update_xaxes(showgrid=False)
fig.update_yaxes(range=(0, 200))
fig.update_xaxes(showline=True, linewidth=1, linecolor='rgb(0, 106, 76)')
fig.update_yaxes(showline=True, linewidth=1, linecolor='rgb(0, 106, 76)')
fig.update_yaxes(
      title='Immunization Clients Seen Per Month',
      zeroline=True,
      showline=True,
      showticklabels=True,
      gridwidth=1
   ),

fig1 = px.scatter(df, x='Year', y='FPClientsSeenPerMonth')
fig1.update_layout(title="FAMILY PLANNING CLINIC MONTHLY PERFORMANCE FOR ORANGEFARM",
                   font=dict(
                       family="Times New Roman,Times,serif",
                       size=13,
                       color="#231F20",
                   ))
fig1.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig1.layout.plot_bgcolor = '#FFFFFF'
fig1.layout.paper_bgcolor = '#fff'
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(range=(0, 70))
fig1.update_xaxes(showline=True, linewidth=1, linecolor='rgb(0, 106, 76)')
fig1.update_yaxes(showline=True, linewidth=1, linecolor='rgb(0, 106, 76)')
fig1.update_yaxes(
      title='FP Clients Seen Per Month',
      zeroline=True,
      showline=True,
      showticklabels=True,
      gridwidth=1
   ),

fig2 = px.scatter(df, x='Year', y='CurativeClientsSeenPerMonth')
fig2.update_layout(title="CURATIVE CARE CLINIC  MONTHLY PERFORMANCE FOR ORANGEFARM",
                   font=dict(
                       family="Times New Roman,Times,serif",
                       size=13,
                       color="#231F20",
                   ))
fig2.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig2.layout.plot_bgcolor = '#FFFFFF'
fig2.layout.paper_bgcolor = '#fff'
fig2.update_xaxes(showgrid=False)
fig2.update_yaxes(range=(0, 100))
fig2.update_xaxes(showline=True, linewidth=1, linecolor='rgb(0, 106, 76)')
fig2.update_yaxes(showline=True, linewidth=1, linecolor='rgb(0, 106, 76)')
fig2.update_yaxes(
      title='Curative Clients Seen Per Month',
      zeroline=True,
      showline=True,
      showticklabels=True,
      gridwidth=1
   ),

fig3 = px.scatter(df, x='Year', y='ANCClientsSeenPerMonth')
fig3.update_layout(title="ANTENATAL CARE CLINIC  MONTHLY PERFORMANCE FOR ORANGEFARM",
                   font=dict(
                       family="Times New Roman,Times,serif",
                       size=13,
                       color="#231F20",
                   ))
fig3.update_traces(mode='markers+lines', marker_color='rgb(0, 106, 76)')
fig3.layout.plot_bgcolor = '#FFFFFF'
fig3.layout.paper_bgcolor = '#fff'
fig3.update_xaxes(showgrid=False)
fig3.update_yaxes(range=(0, 30))
fig3.update_xaxes(showline=True, linewidth=1, linecolor='rgb(0, 106, 76)')
fig3.update_yaxes(showline=True, linewidth=1, linecolor='rgb(0, 106, 76)')
fig3.update_yaxes(
      title='ANC Clients Seen Per Month',
      zeroline=True,
      showline=True,
      showticklabels=True,
      gridwidth=1
   ),

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_orangefarm_menu(),
    html.H3('ORANGEFARM MONTHLY DATA VISUALIZATION',
            style={"font-weight": "bold", "text-align": "center", "font-size": "18px",
                   'family': "Times New Roman,Times,serif", }),
    html.Div([dash_table.DataTable(

                            id='Desc',
                            columns=[{"Facility name": i, "id": i} for i in df1.columns],
                            data=df1.to_dict('records'),
                            style_table={'Height': 200, 'Width': 100, 'overflowX': 'auto'},
                            style_header={
                                'backgroundColor': 'white',
                                'fontWeight': 'bold',
                                'font-family': "Times New Roman,Times,serif",
                            },
                            style_cell={'textAlign': 'Center', 'overflow': 'hidden',
                                        'fontSize': 14,
                                        'textOverflow': 'ellipsis',
                                        # all three widths are needed
                                        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                        'whiteSpace': 'normal',
                                        'background': 'white',
                                        'padding': '10px',
                                        'font-family': "Times New Roman,Times,serif",
                                        'border-style': 'solid',

                                        },
                            style_data={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                        'lineHeight': '15px',
                                        'fontSize': 14,
                                        'textOverflow': 'ellipsis',
                                        'padding': '5px',
                                        'font-family': "Times New Roman,Times,serif",

                                    },
                        ),]),

    html.Div(
        dbc.Card('Indicator Summary', color="White", className="me-1",
                 style={"font-size": "18px",
                        'font-family': "Times New Roman,Times,serif"}, ), ),


    dbc.Row([
        dbc.Col([card]), dbc.Col([card1]), dbc.Col([card2]), dbc.Col([card3]), dbc.Col([card4])
    ]),

    ##Differntiating Tab between indicator summary and the graphs.
    #commonmodules.get_diff_menu(),
    html.Div(
        dbc.Card('', color="White", className="me-1",
                 style={"font-size": "18px"}, ), ),

    #Graph Display Section
    html.Div(
        [html.Label(),
         dcc.Graph(
         id='Immunization-graph',
         figure=fig
                  ),]),

    html.Label(),
    dcc.Graph(
        id='fp-graph',
        figure=fig1
    ),
    html.Label(),
    dcc.Graph(
        id='Curative-graph',
        figure=fig2
    ),
    html.Label(),
    dcc.Graph(
        id='ANC-graph',
        figure=fig3
    ),

]),


##################################################################################################

main_page = dbc.Container([layout],fluid = True)
