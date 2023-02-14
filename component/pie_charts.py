from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from util import get_gender, get_mar, get_stay_year
import matplotlib.pyplot as plt
from ids import *


def render(app):
    df = get_gender()
    fig = px.pie(df, values='Purchase', names='Gender', title='Gender With Total Purchase', labels={'Gender': 'Gender Type'})
    return html.Div(dcc.Graph(figure=fig), id= PIE_CHART )

def render1(app):
    df = get_mar()
    fig = px.pie(df, values='Purchase', names='Marital_Status', title='Marital Status With Total Purchase', labels={'Marital_Status': 'Marital_Status Type'}) 
    return html.Div(dcc.Graph(figure=fig),id= PIE_CHART1 )

def render2(app):
    df = get_stay_year()
    fig = px.pie(df, values='Purchase', names='Stay_In_Current_City_Years', title='Stay years With Total Purchase', labels={'Stay_In_Current_City_Years': 'Stay_In_Current_City_Years Type'}) 
    return html.Div(dcc.Graph(figure=fig),id= PIE_CHART2 )