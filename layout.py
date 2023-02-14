from dash import Dash,html
import dash_bootstrap_components as dbc
from component import pie_charts, bar_charts

imapath = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkwvfZ6q2ZlwXlLgbAdvCgT9pFComtUicw4A&usqp=CAU"

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.P(children="🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥✨✨✨✨✨✨✨", className="header-emoji"),
        html.H1(
                "Black Friday Analytics", className="header-title"
              ),
        html.P(
                "Based on black friday data set we can analyze which group is our main customer.",
                className="header-description",
                ),
        html.Img(src=imapath, style={"width": "1500px", "height": "300px"})
,         
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(pie_charts.render(app),lg=6),
            dbc.Col(bar_charts.render(app),lg=6),
            dbc.Col(pie_charts.render1(app),lg=6),
            dbc.Col(bar_charts.render1(app),lg=6),
            dbc.Col(pie_charts.render2(app),lg=6),
            dbc.Col(bar_charts.render2(app),lg=6)

        ],className="mt-4")
    ])