import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Global parameters of colors
colors = {

    'background': '#FDEBD0', # Beige
    'text': '#C0392B' # Red

}

markdown_text = """

## Markdown Text

* testing one two
* do visit my notebook at my [GitHub](https://www.github.com/jasonchanhku)


"""

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode="markers"
)

trace2 = go.Scatter(
    x=random_x,
    y=random_y,
    mode="markers",
    marker=dict(
        color='#5D6D7E'
    )
)

# children is always the first argument, and is usually omitted

app.layout = html.Div(style={'backgroundColor': colors['background'], 'columnCount': 1}, children=[

    html.H1(
        children="Hello Dash",
        style={

            'textAlign': 'center',
            'color': colors['text']
        }


    ),

    html.Div(
        children="""
                    Dash: A web application framework for Python
                """,
        style={

            'textAlign': 'center',
            'color': colors['text']
        }

    ),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                # Graph background color
                'plot_bgcolor': colors['background'],
                # Remaining background color
                'paper_bgcolor': colors['background'],
                # Color of graph title
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),

    dcc.Markdown(children=markdown_text),

    dcc.Graph(
        id="scatterplot",
        figure={
            'data': [trace],
            'layout':{
                'title': 'Scatterplot',
                # Graph background color
                'plot_bgcolor': colors['background'],
                # Remaining background color
                'paper_bgcolor': colors['background'],
                # Color of graph title
                'font': {
                    'color': colors['text']
                }

            }
        }

    ),

    dcc.Graph(
        id="scatterplot2",
        figure={
            'data': [trace2],
            'layout': {
                'title': 'Scatterplot 2',
                # Graph background color
                'plot_bgcolor': colors['background'],
                # Remaining background color
                'paper_bgcolor': colors['background'],
                # Color of graph title
                'font': {
                    'color': colors['text']
                }

            }
        }

    ),

    html.Label("Choose a Dropdown"),

    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
            ],
        value='MTL',

        ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )


])

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == "__main__":
    app.run_server(debug=True)