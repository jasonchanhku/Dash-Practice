# Having two dccs in the same line
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import search_google.api
from dash.dependencies import Input, Output


def get_fighter_url(fighter):
    buildargs = {
      'serviceName': 'customsearch',
      'version': 'v1',
      'developerKey': 'AIzaSyAQACPWQ00cwV72F3YIOP70RqqkyZyBaUQ'
    }

    # Define cseargs for search
    cseargs = {
      'q': fighter + '' + 'Official Fighter Profile',
      'cx': '007364733105595844420:eu9ova5tqdg',
      'num': 1,
      'searchType':'image',
      'imgType':'clipart',
      'fileType':'png',
      'safe': 'off'
    }

    # Create a results object
    results = search_google.api.results(buildargs, cseargs)
    url = results.links[0]
    return(url)

colors = {

    'background': '#F4F6F7',
    'text': '#34495E'

}

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'cb5392c35661370d95f300086accea51/raw/'
    '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
    'indicators.csv')

available_indicators = df['Indicator Name'].unique()

app = dash.Dash()

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1(
        "UFC MMA Predictor v1.0",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),


    html.Center(

        html.Div(style={'width': '40%'}, children=[

            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in ['Lightweight', 'Welterweight']],
                value='Lightweight'
            )


        ])

    ),

    html.Br(),

    html.Div(style={'width': '40%', 'display': 'inline-block'}, children=[

        dcc.Dropdown(
            id='xaxis-column',
            options=[{'label': i, 'value': i} for i in ['Conor McGregor', 'Tony Ferguson']],
            value='Tony Ferguson'
        ),

        dcc.RadioItems(
            id='xaxis-type',
            options=[{'label': i, 'value': i} for i in ['Favourite', 'Underdog']],
            value='Linear',
            labelStyle={'display': 'inline-block'}
            # inline blockmakes the buttons in one line horizontally rather than vertically
        ),

        html.Img(
            src=get_fighter_url('Tony Ferguson')
        )


    ]),

    html.Div(style={'width': '40%', 'float': 'right', 'display': 'inline-block'}, children=[

      dcc.Dropdown(
          id='yaxis-column',
          options=[{'label': i, 'value': i} for i in ['Conor McGregor', 'Tony Ferguson']],
          value='Conor McGregor'
      ),

      dcc.RadioItems(
          id='yaxis-type',
          options=[{'label': i, 'value': i} for i in ['Favourite', 'Underdog']],
          value='Linear',
          labelStyle={'display': 'inline-block'}
      ),

      html.Img(
            src=get_fighter_url('Conor Mcgregor')
       )

    ]),

    html.Br(),

    html.Br(),

    html.Center(
        html.Div(style={'width': '10%', 'margin': 'auto', 'display': 'inline-block'}, children=[

            html.H2("VS",
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                    )

        ])
    )



])

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == "__main__":
    app.run_server(debug=True)
