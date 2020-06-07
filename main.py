import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
from apps import overview, privacy

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1('Navigation'),
    html.Br(),
    dcc.Link('Overview', href='/'),
    html.Br(),
    dcc.Link('Privacy ', href='/privacy'),
    html.Br(),
    html.Br(),
    # page content from respective site will be loaded via this id
    html.Div(id='page-content')
])

server = app.server


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return overview.layout
    if pathname == '/privacy':
        return privacy.layout
    else:
        print(pathname)
        return '404'


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8080)
