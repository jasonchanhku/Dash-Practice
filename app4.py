import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import os

colors = {

    'background': '#F4F6F7',
    'text': '#34495E'

}

app = dash.Dash(__name__)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1('Dash Interactivity with Chained Multiple Outputs',

            style={
                'textAlign': 'center',
                'color': colors['text']
            }

            ),

    dcc.RadioItems(
        id='countries-dropdown',
        # Gets the keys of all_options as label and values for RadioItems
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='America'

    ),

    # Thematic break
    html.Hr(),

    # This is the component we want to change based on what we choose in first radio items
    dcc.RadioItems(
        id='cities-dropdown'
    ),

    html.Hr(),

    html.Div(id='display-selected-values'),

    html.Center(

        html.Img(
        # align = "middle" is vertical alignment, need to wrap it around <center> img </center>
        src='http://vignette4.wikia.nocookie.net/mixedmartialarts/images/c/c5/UFC_logo.png/revision/latest?cb=20130511014401'
    )
    )

])


# Filters the second radio button after selecting out country in countries-dropdown
# Note that this returns a dictionary
# We still need another callback function to set the value


@app.callback(
    Output('cities-dropdown', 'options'),
    [Input('countries-dropdown', 'value')]
)
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

# From the filtered dictionary, return the value as the value we clicked from the second radio
# available_options[0] is the only row available
# callback function called everytime cities-dropdown options changed
# This implies the value changes as well


@app.callback(
    Output('cities-dropdown', 'value'),
    [Input('cities-dropdown', 'options')]
)
def set_cities_values(available_options):
    return available_options[0]['value']

# We need a third callback function to print
# based on the the variables that we updated

# Only one [], nested Input
@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-dropdown', 'value'),
     Input('cities-dropdown', 'value')])
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)