from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from util import get_age, get_mar, get_occ, get_stay_year, get_city
import matplotlib.pyplot as plt
from ids import *

def render(app):
    df = get_age()
    fig = px.bar(df, x='Age', y='Purchase') 
    return html.Div(dcc.Graph(figure=fig),id=BAR_CHART)

def render1(app):
    df = get_occ()
    fig = px.bar(df, x='Occupation', y='Purchase') 
    return html.Div(dcc.Graph(figure=fig),id=BAR_CHART1)

def render2(app):
    df = get_city()
    fig = px.bar(df, x='City_Category', y='Purchase') 
    return html.Div(dcc.Graph(figure=fig),id=BAR_CHART2)