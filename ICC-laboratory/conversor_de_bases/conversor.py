import dash
from dash import dcc, Input, Output, html, State
import dash_bootstrap_components as dbc
from styles import Styles

# class Styles:
        
#         page = {
#              'width':'100%',
#              'display':'flex',
#              'flex-direction':'column',
#              'gap':'80px',
#              'align-items':'center',
#              'justify-content':'center',
#              'height':'100%'}

#         header = {
#              'background-color':'#E72313',
#              'width':'100%'
#         }

#         headerText = {
#             'color': '#FFF',
#             'font-size': '32px',
#             'font-style': 'bold',
#             'font-weight': '700',
#             'line-height': 'normal',
#             'padding-left':'1%'
#         }

#         card = {
#             'width':'70%',
#             'height':'768px',
#             'border-radius': '20px',
#             'background':'#FFF',
#             'box-shadow' : '0 0px 20px 0 rgba(0, 0, 0, 0.25)',
#         }

#         cardChildren = {
#              'display':'flex',
#              'flex-direction':'column',
#              'align-items' : 'center'
#         }

#         title = {
#              'display' : 'flex',
#              'align-items':'center',
#              'padding':'3%',
#              'width':'100%'
#         } 

#         titleText = {
#             'color' : '#000',
#             'font-size' : '32px',
#             'font-style' : 'bold',
#             'font-weight' : '700',
#             'line-height' : 'normal',
#             'padding-left' :'1%'
#         }

#         inputsParent = {
#              'display':'flex',
#              'flex-direction':'row',
#              'justify-content':'center',
#              'width':'100%',
#              'justify-content':'space-evenly',
#              'align-items':'center'
#         }

#         inputs = {
#             'marging-left':'9%',
#             'marging-right':'9%',
#             'padding-bottom':'6%',
#             'width' : '20%'
#         }

#         buttonsParent = {
#              'display':'flex',
#              'flex-direction':'column',
#              'padding-left':'9%',
#              'width':'100%'
#         }

#         buttons = {
#             'width':'20%'
#         }

#         outputParent = {
#              'display':'flex',
#              'flex-direction':'column',
#              'padding-left':'9%',
#              'padding-top':'3%',
#              'width':'100%'
#         }

#         outputTitle = {
#             'font-size': '24px',
#             'font-style': 'normal',
#             'font-weight': '700',
#             'line-height': 'normal'
#         }

#         outputText = {
#             'color': '#E72313',
#             'font-size': '128px',
#             'font-style': 'normal',
#             'font-weight': '700',
#             'line-height': 'normal',
#         }

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
 
    # Header
    html.Div([
        dbc.Label('Laboratório ICC', style=Styles.headerText)
    ], style=Styles.header),

    # Card
    html.Div([

        html.Div([
            
            # Title
            html.Div([

                html.Img(src=r'assets/logo.png', alt='image'),
                html.H3('Conversor de bases numéricas', style={'padding-left':'1%'})

            ], style=Styles.title),

            # Inputs
            html.Div([
                html.Div([

                    dbc.Label('Número:', style=Styles.inputsLabels),
                    dbc.Input(placeholder = 'Digite um valor inteiro', valid = True, id = 'input-num', type = 'text'),
                    dbc.FormText('*Valores entre as bases 2-36')

                ], style=Styles.inputs),

                html.Div([

                    dbc.Label('Base Inicial:', style=Styles.inputsLabels),
                    dbc.Input(placeholder = 'Digite um valor inteiro', valid = True, id = 'input-baseI', type = 'number'),
                    dbc.FormText('*Valor entre 2-36')

                ], style=Styles.inputs),

                html.Div([

                    dbc.Label('Base Final:', style=Styles.inputsLabels),
                    dbc.Input(placeholder = 'Digite um valor inteiro', valid = True, id = 'input-baseF', type = 'number'),
                    dbc.FormText('*Valor entre 2-36')
                ], style=Styles.inputs),

            ], style=Styles.inputsParent),

            # Buttons
            html.Div([

                dbc.Button('CALCULAR', color = 'danger', id = 'Calcular', style=Styles.buttons, n_clicks=0),
                dbc.Button('RESETAR', color = 'danger', id = 'Resetar', outline = True, style=Styles.buttons, n_clicks=0)

            ], style=Styles.buttonsParent),

            # Output
            html.Div([

                dbc.Label(
                    'Resultado: ',
                    style=Styles.outputTitle
                ),
                dbc.Label(
                    children = 'Resultado',
                    id = 'output_result',
                    style=Styles.outputText
                )

            ], style=Styles.outputParent),

        ], style=Styles.cardChildren)

    ], style=Styles.card)

], style=Styles.page)

@app.callback([
    Output('output_result', 'children', allow_duplicate=True),
    [Input('Calcular','n_clicks'),
     State('input-num', 'value'),
     State('input-baseI', 'value'),
     State('input-baseF', 'value')],
],prevent_initial_call = True,)
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

@app.callback([
    Output('input-num', 'value'),
    Output('input-baseI', 'value'),
    Output('input-baseF', 'value'),
    Output('output_result', 'children'),
    [Input('Resetar', 'n_clicks')]
])
def reset(n_clicks):
    return (None, None, None, 'Resultado')

@app.callback([
    Output('input-num', 'valid'),
    [Input('input-num', 'value')]
], prevent_initial_call = True)
def validateInputs(text):
    try:
        for letra in text:
            if letra in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                return [True]
            else:
                return [False]
    except:
        return [False]
        
if __name__ == '__main__':
    app.run_server(debug = True)
