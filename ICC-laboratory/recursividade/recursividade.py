from time import sleep
import os
from colored import Style, Fore

def menu():
    qnt_caracter = 20
    print('=-'*qnt_caracter)
    print(f'{Fore.green}' + f'LABORATÓRIO ICC'.center(qnt_caracter*2) + f'{Style.reset}')
    print('RECURSIVIDADE'.center(qnt_caracter*2))
    print('=-'*qnt_caracter)

def loading():
    print('\033[1A'*3)
    for temp in range(3):
        for idx in range(len(palavra:='CARREGANDO...')):
            print(palavra[:idx+1].center(40), end='\r')
            sleep(0.07)
        print('\x1b[2K', end='') 
    # print('\033[1A'*2)

def inputNum():
    while True:
        try: # Barra não números e números com casas decimais válidas ex.: 1.001
            numero = float(input(f'Número: {Fore.green}').replace(',','.'))# Permite decimais de acordo com a escrita brasileira
            print(f'{Style.reset}')
            if numero % 1 == 0: # Permite números com casa decimais inválidas ex.: 1.00000
                numero = int(numero)
                return numero
            else:
                print('Insira um valor válido:')

        except: 
            print(numero % 1)
            print('Insira um valor válido:')

def fatInterativo(num):
    fat = 1

    if num in [0,1]:
        return fat
    
    else:
        for c in range(num,1,-1):
            fat *= c
        return fat

def fatRecursivo(num):
    fat = 1

    if num in [0,1]:
        pass
    else:
        fat *= num * fatRecursivo(num-1)

    return fat

def mostrarResult(num, resultI, resultR):
    qnt_caracter = 20
    print(f'FATORIAL DE {num}'.center(qnt_caracter*2))
    print(f'MODO INTERATIVO: {resultI}'.center(qnt_caracter*2))
    print(f'MODO RECURSIVO: {resultR}'.center(qnt_caracter*2))
    print('=-'*qnt_caracter)

def continuar():
    while True:
        if (resp:=input(f'Deseja calcular outro fatorial? [{Fore.green}S{Style.reset}/{Fore.red}N{Style.reset}] ').upper()) in ['S', 'N']:
            return True if resp == 'S' else False
        else:
            print('\033[1A'*2)
            print('Insira uma resposta válida.'. ljust(50))
            sleep(0.2)

if __name__ == '__main__':
    while True:
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
            os.system('cls')
            sleep(.5)