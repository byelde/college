import dash
from dash import dcc, Input, Output, html, State
import dash_bootstrap_components as dbc


class Styles:
        header = {
            'display': 'flex',
            'background-color': '#E72313',
            'width':'100%',
            'height':'96px',
        }

        headerText = {
            'color': '#FFF',
            'font-size': '32px',
            'font-style': 'bold',
            'font-weight': '700',
            'line-height': 'normal',
            'padding-left':'1%'
        }

        card = {
            'width':'70%',
            'height':'768px',
            'border-radius': '20px',
            'background':'#FFF',
            'box-shadow' : '0 0px 20px 0 rgba(0, 0, 0, 0.25)',
        }

        titleText = {
            'color' : '#000',
            'font-size' : '32px',
            'font-style' : 'bold',
            'font-weight' : '700',
            'line-height' : 'normal',
            'padding-left' :'1%'
        }

        inputs = {
            'marging-left':'9%',
            'marging-right':'9%',
            'padding-bottom':'6%',
            'width' : '20%'
        }

        buttons = {
            'width':'20%'
        }

        outputTitle = {
            'font-size': '24px',
            'font-style': 'normal',
            'font-weight': '700',
            'line-height': 'normal'
        }

        outputText = {
            'color': '#E72313',
            'font-size': '128px',
            'font-style': 'normal',
            'font-weight': '700',
            'line-height': 'normal',
        }

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
 
    # Header
    html.Div([
        dbc.Label('Laboratório ICC', style=Styles.headerText)
    ], style={'background-color':'#E72313', 'width':'100%'}),

    # Card
    html.Div([

        html.Div([
            
            # Title
            html.Div([

                html.Img(src=r'assets/logo.png', alt='image'),
                html.H3(
                        'Conversor de bases numéricas.',
                        style={'padding-left':'1%'}
                )

            ], style={'display' : 'flex', 'align-items':'center', 'padding':'3%', 'width':'100%'}),

            # Inputs
            html.Div([
                html.Div([

                    dbc.Label('Número:'),
                    dbc.Input(placeholder = 'Digite um valor inteiro', id = 'input-num', type = 'number'),
                    dbc.FormText('*Valores entre as bases 2-36')

                ], style=Styles.inputs),

                html.Div([

                    dbc.Label('Base Inicial:'),
                    dbc.Input(placeholder = 'Digite um valor inteiro', id = 'input-baseI', type = 'number'),
                    dbc.FormText('*Valor entre 2-36')

                ], style=Styles.inputs),

                html.Div([

                    dbc.Label('Base Final:'),
                    dbc.Input(placeholder = 'Digite um valor inteiro', id = 'input-baseF', type = 'number'),
                    dbc.FormText('*Valor entre 2-36')
                ], style=Styles.inputs),

            ], style={'display':'flex', 'flex-direction':'row', 'justify-content':'center', 'width':'100%', 'justify-content':'space-evenly', 'align-items':'center'}),

            # Buttons
            html.Div([

                dbc.Button('CALCULAR', color = 'danger', id = 'Calcular', style=Styles.buttons, n_clicks=0),
                dbc.Button('RESETAR', color = 'danger', id = 'Resetar', outline=True, style=Styles.buttons, n_clicks=0)

            ], style={'display':'flex', 'flex-direction':'column', 'padding-left':'9%', 'width':'100%'}),

            # Output
            html.Div([

                dbc.Label(
                    'Resultado: ',
                    style=Styles.outputTitle
                ),
                dbc.Label(
                    children = 'Resultado.',
                    id = 'output_result',
                    style=Styles.outputText
                )

            ], style={'display':'flex', 'flex-direction':'column', 'padding-left':'9%', 'padding-top':'3%', 'width':'100%'}),

        ], style={'display':'flex', 'flex-direction':'column', 'align-items' : 'center', })

    ], style=Styles.card)

], style={'width':'100%', 'display':'flex', 'flex-direction':'column','gap':'80px', 'align-items':'center', 'justify-content':'center', 'height':'100%'})

@app.callback([
    (Output('output_result', 'children')),
    [Input('Calcular','n_clicks'),
     State('input-num', 'value'),
     State('input-baseI', 'value'),
     State('input-baseF', 'value')]
])
def converter(nclicks, num, bi, bf):

    num, bi, bf = str(num), int(bi), int(bf)

    num = num[::-1]

    db = '0123456789abcdefghijklmnopqrstuvwxyz'

    # Para base 10

    na10 = 0

    for idx_digito, digito in enumerate(num):
        for idx_db, db_digito in enumerate(db):
            if digito == db_digito:
                na10 += ((int(bi)**idx_digito)*int(idx_db))

    # Para a base final (bf)

    nabf = ''

    while True:
         
        if na10 < bf:
            for idx_db, db_digito in enumerate(db):
                  if str(na10) == str(idx_db):
                       nabf += db_digito.upper()
                       break
            break

        
        for idx_db, db_digito in enumerate(db):
            if idx_db == na10%bf:
                nabf += str(db_digito).upper()
                na10 = na10//bf
                break


    return [nabf[::-1]]


if __name__ == '__main__':
    app.run_server(debug = True)
