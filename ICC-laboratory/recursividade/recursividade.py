from time import sleep
import os
from colored import Style, Fore

def posCursor(l,c=0):
    print(f'\033[{l};{c}H')

def limparLinha():
    print('\033[K', end='')

def menu():

    qnt_caracter = 20

    print('=-'*qnt_caracter)
    print(f'{Fore.green}' + f'LABORATÓRIO ICC'.center(qnt_caracter*2) + f'{Style.reset}')
    print('RECURSIVIDADE'.center(qnt_caracter*2))
    print('=-'*qnt_caracter)

def loading():

    posCursor(4)

    for temp in range(3):
        for idx in range(len(palavra:='CARREGANDO...')):
            print(palavra[:idx+1].center(40), end='\r')
            sleep(0.07)
        limparLinha() 

def inputNum():
    while True:
        try: # Barra não números

            numero = float(input(f'Número: {Fore.green}').replace(',','.')) # Permite decimais de acordo com a escrita brasileira

            print(f'{Style.reset}')
            posCursor(5)
            limparLinha()
            posCursor(4)

            if numero % 1 == 0 and numero>= 0: # Permite números com casa decimais inválidas ex.: 1.00000
                numero = int(numero)
                return numero
            
            else:
                print('Insira um valor válido.')

        except Exception as er: 

            print(f'{Style.reset}')
            posCursor(4)
            print('Insira um valor válido.')
        
        limparLinha()
        sleep(0.3)

def fatInterativo(num):
    fat = 1

    if not num in [0,1]:
        for c in range(num,1,-1):
            fat *= c

    return fat

def fatRecursivo(num):

    return (num * fatRecursivo(num-1)) if not num in [0,1] else 1

def mostrarResult(num, resultI, resultR):

    qnt_caracter = 20
    msgs = [f'MODO INTERATIVO: {resultI}',
            f'MODO RECURSIVO: {resultR}']
    

    print(f'FATORIAL DE {num}'.center(qnt_caracter*2))

    for msg in (msgs):
        if len(msg) >= 35:
            msg = (msg[:35] +'...').center(qnt_caracter*2)
        print(msg.center(qnt_caracter*2))        

    print('=-'*qnt_caracter)

def continuar():

    while True:

        if (resp:=input(f'Deseja calcular outro fatorial? [{Fore.green}S{Style.reset}/{Fore.red}N{Style.reset}] ').upper()) in ['S', 'N']:
            return True if resp == 'S' else False
        
        else:
            posCursor(8)
            print('Insira uma resposta válida.'. ljust(50))
            sleep(0.2)

if __name__ == '__main__':

    while True:
        os.system('cls')

        menu()
        n = inputNum()
        loading() # Apenas estético
        interativo = fatInterativo(n)
        recursivo = fatRecursivo(n)
        mostrarResult(n, interativo, recursivo)

        if not continuar():
            print('Até a próxima :)')
            break
        else:
            sleep(.5)