import dash
from dash import dcc, Input, Output, html
import dash_bootstrap_components as dbc

def criarDB():

    DB = {}
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for n in range(10):
        DB[str(n)] = str(n)

    for n in range(10,36):
        DB[str(alfabeto[n-10])] = str(n)

    return DB

def inputNum():

    while True:

        try:

            number = input('Número: ').split('.')
            iBase = int(input('Base: '))
            fBase = int(input('Para base: '))
            return iBase, fBase, number
        
        except Exception as er:

            # print(er)
            print('Insira valores válido.')    

def toTen(b, num, DB):

    # Parte inteira:

    partInt_i = num[0][::-1]
    partInt_C = 0

    for idx, digito in enumerate(partInt_i):
        partInt_C += int(DB[digito.upper()])*(b**idx)


    return partInt_C

def tenToB(b, num, DB):

    numConvertido = ''

    # Parte inteira

    while True:

        for index, value in DB.items():
            if value == str(num%b):
                numConvertido += index
                break

        num = num//b

        if num < b:
            for index, value in DB.items():
                if value == str(num):
                    numConvertido += index
                    break
            break

    return numConvertido[::-1]
    
def conversor():

    db = criarDB()
    init_base, final_base, init_num = inputNum()
    num_base10 = toTen(init_base, init_num, db)
    return tenToB(final_base, num_base10, db)

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

                dbc.Button('CALCULAR', color = 'danger', id = 'Calcular', style=Styles.buttons),
                dbc.Button('RESETAR', color = 'danger', id = 'Resetar', outline=True, style=Styles.buttons)

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

], style={'width':'100%', 'display':'flex', 'flex-direction':'column', 'align-items':'center', 'justify-content':'center'})

if __name__ == '__main__':
    app.run_server(debug = True)
