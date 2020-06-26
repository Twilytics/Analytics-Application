import pandas as pd
import dash_html_components as html
from database_conncetion import connect
import dash_table

# connect to database and add files to
conn = connect()
sql = "select * from postgres.public.account;"
df = pd.read_sql_query(sql, conn)
df = df.head(10)
conn = None

layout = html.Div(children=[
    html.H1(children='Overview'),

    html.Div(children='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                      'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                      'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                      'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat '
                      'non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'),

    html.Div(dash_table.DataTable(
                id='table-2',
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.loc[:]
                         ],
    ),)
])
