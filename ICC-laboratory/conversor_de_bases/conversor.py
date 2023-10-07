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
            'font-family': 'Kantumruy',
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
            'box-shadow' : '0 0px 20px 0 rgba(0, 0, 0, 0.25)'
        }

        titleText = {
            'color': '#000',
            'font-family': 'Kantumruy',
            'font-size': '32px',
            'font-style': 'bold',
            'font-weight': '700',
            'line-height': 'normal',
            'padding-left':'1%'
        }

app = dash.Dash(__name__)

app.layout = dbc.Container([
    dbc.Row([
        html.P('Laboratório ICC', style=Styles.headerText)
    ], style=Styles.header),

    dbc.Row([
        html.Div([

            dbc.Row([
                html.P('Conversor de bases numéricas', style=Styles.titleText)
            ]),

            dbc.Row([

            ]),

            dbc.Row([

            ]),

            dbc.Row([

            ]),
        ], style=Styles.card)
    ], style={'align-items':'center'}),
])

if __name__ == '__main__':
    app.run_server(debug = True)
