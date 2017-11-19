import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

colors = {

    'background': '#F4F6F7',
    'text': '#34495E'

}
# Remember that dash has two components, the layout part and the interactivity part

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1('Part 2: Interactivity in Dash',

            style={
                'textAlign': 'center',
                'color': colors['text']
            }

            ),
    dcc.Input(id='my-id', value='initial value', type='text'),

    html.Div(id='my-div')


])

# Decorator for our function below
# Whenever input changes, function that callback decorator wraps will be called
# Every dash component is described entirely with keyword arguments
# These can be changed dynamically via a callback decorator
# Similar to excel programming


@app.callback(
    # Inputs and Outputs declared declaratively
    # Output is our 'children' property of 'my-div'
    Output('my-div', 'children'),
    # Input is our 'value' property of my-idc
    [Input('my-id', 'value')]
)
def update_output_value(input_value):
    return 'You have just entered "{}"'.format(input_value)

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == "__main__":
    app.run_server(debug=True)