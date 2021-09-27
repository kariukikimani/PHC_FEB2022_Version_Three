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
meta_tags = [{'name': 'viewport',
              'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}
card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("GOPD TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),

            html.H2("72,005", id="card-value",style={"font-weight": "bold", "text-align": "center", "font-size": "12px",
                           'family': "Times New Roman,Times,serif", "color": "blue", }),
        ],
    )
)
card1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("CWC TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("11,697", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                   'family': "Times New Roman,Times,serif", "color": "blue",}),
        ]
    )
)
card2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("ANC TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("5,341", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                   'family': "Times New Roman,Times,serif","color": "blue", }),
        ]
    )
)
card3 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("PNC TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("1,707", id="card-value", style={"font-weight": "bold", "text-align": "center", "font-size": "12px",
                                                     'family': "Times New Roman,Times,serif", "color": "blue", }),
        ]
    )
)
card4 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("FP TOTAL SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("3,916", id="card-value", style={"font-weight": "bold","text-align": "center", "font-size": "12px",
                                                     'family': "Times New Roman,Times,serif" , "color": "blue", }),
        ]
    )
)
card5 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("TOTAL DELIVERIES SINCE LAUNCH", id="card-title",
                    style={"font-weight": "bold", "text-align": "center", "font-size": "13px",
                           'family': "Times New Roman,Times,serif", }),
            html.H2("2,340", id="card-value", style={"font-weight": "bold", "text-align": "center", "font-size": "12px",
                                                     'family': "Times New Roman,Times,serif", "color": "blue", }),
        ]
    )
)

card6 = dbc.Card(
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
df = pd.read_csv('data/Dandu_Data.csv')
df1 = pd.read_csv('data/Dandu_Facility_Information_Data.csv')

fig = px.scatter(df, x='Year', y='GOPD_CLIENTS_SEEN_PER_MONTH')
fig.update_traces(mode='markers+lines')

fig1 = px.scatter(df, x='Year', y='CWC_CLIENTS_SEEN_PER_MONTH')
fig1.update_traces(mode='markers+lines')

fig2 = px.scatter(df, x='Year', y='ANC_CLIENTS_SEEN_PER_MONTH')
fig2.update_traces(mode='markers+lines')

fig3 = px.scatter(df, x='Year', y='PNC_CLIENTS_SEEN_PER_MONTH')
fig3.update_traces(mode='markers+lines')

fig4 = px.scatter(df, x='Year', y='FP_CLIENTS_SEEN_PER_MONTH')
fig4.update_traces(mode='markers+lines')

fig5 = px.scatter(df, x='Year', y='DELIVERIES_COMPLETED_PER_MONTH')
fig5.update_traces(mode='markers+lines')


layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_dandu_menu(),
    html.H3('DANDU MONTHLY DATA VISUALIZATION',
            style={"font-weight": "bold", "text-align": "center", "font-size": "18px",
                   'family': "Times New Roman,Times,serif", }),
    html.Div([dash_table.DataTable(

                            id='Desc',
                            columns=[{"Facility name": i, "id": i} for i in df1.columns],
                            data=df1.to_dict('records'),
                            style_table={'Height': 200, 'Width': 100, 'overflowX': 'auto'},
                            style_header={
                                'backgroundColor': 'light-blue',
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
        dbc.Col([card]), dbc.Col([card1]), dbc.Col([card2]), dbc.Col([card3]), dbc.Col([card4]), dbc.Col([card5]), dbc.Col([card6])
               ]),
    html.Div(
        [html.Label(["GOPD MONTHLY PERFORMANCE"],
                    style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                           'family': "Times New Roman,Times,serif", }),
             dcc.Graph(
             id='GOPD-graph',
             figure=fig
    ),]),

    html.Label(["CWC MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='CWC-graph',
        figure=fig1
    ),
    html.Label(["ANC MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='ANC-graph',
        figure=fig2
    ),
    html.Label(["PNC MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='PNC-graph',
        figure=fig3
    ),
    html.Label(["FP MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='FP-graph',
        figure=fig4
    ),
    html.Label(["DELIVERIES MONTHLY PERFORMANCE"],
               style={"font-weight": "bold", "text-align": "left", "font-size": "12px",
                      'family': "Times New Roman,Times,serif", }),
    dcc.Graph(
        id='Deliveries-graph',
        figure=fig5
    ),

]),


##################################################################################################

main_page = dbc.Container([layout],fluid = True)
