import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Data loading should be done globally instead of in the decorator, this ensure process only done once
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash()

colors = {

    'background': '#F4F6F7',
    'text': '#34495E'

}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1('Part 3: Interactivity in Dash',

            style={
                'textAlign': 'center',
                'color': colors['text']
            }

            ),

    html.H2("Scatterplot of Life Expectency vs GDP Per Capita",

            style={
                'textAlign': 'center',
                'color': colors['text']
            }
            ),

    dcc.Graph(id='graph-with-slider'),

    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        step=None,
        # Generates key and values accordingly, important for project
        marks={str(year): str(year) for year in df['year'].unique()}

    )

])


# Callback decorator that will call function below
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')]
)
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i

        ))

    return dict(data=traces, layout=go.Layout(
        xaxis={'type': 'log', 'title': 'GDP Per Capita'},
        yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
        legend={'x': 0, 'y': 1},
        hovermode='closest',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],

    ))

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == "__main__":
    app.run_server(debug=True)
