#imports
from os import system

#funções
def menu():
    print('-='*15)
    print('[1] Adição')
    print('[2] Subtração')
    print('[3] Multiplicação')
    print('[4] Divisão')
    print('[5] Sair')
    print('-='*15)

def soma(a):
    for c in range(1,11):
        print(f'{a} + {c} = {a+c}')
    x = input('Digite algo para sair: ')
    system('cls')

def sub(a):
    for c in range(1,11):
        print(f'{a} - {c} = {a-c}')
    x = input('Digite algo para sair: ')
    system('cls')

def multi(a):
    for c in range(1,11):
        print(f'{a} x {c} = {a*c}')
    x = input('Digite algo para sair: ')
    system('cls')

def div(a):
    for c in range(1,11):
        print(f'{a} / {c} = {a/c:.2f}')
    x = input('Digite algo para sair: ')
    system('cls')

#main
while True:
    menu()
    while True:
        op = int(input('Opção: '))
        if not 1 <= op <= 5:
            print('ERRO! Digite um valor válido.')
        else: 
            break

    if op == 1:
        soma(int(input('Valor: ')))
    elif op ==2:
        sub(int(input('Valor: ')))
    elif op ==3:
        multi(int(input('Valor: ')))
    elif op ==4:
        div(int(input('Valor: ')))
    elif op ==5:
        break