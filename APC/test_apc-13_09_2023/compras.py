from os import *

def addProd():
    nome = input('Nome do produto: ')
    valor = float(input('Valor do produto: '))
    qntde = int(input('Quantidade: '))

    lista_de_produtos[nome] = [valor, qntde]

def listProd():
    print('LISTAR')
    total = 0
    for produto in lista_de_produtos:
        print(f'{produto} {lista_de_produtos[produto][1]} x R${lista_de_produtos[produto][0]:.2f} = {lista_de_produtos[produto][1]*lista_de_produtos[produto][0]}')
        total += lista_de_produtos[produto][1]*lista_de_produtos[produto][0]
    print(f'Total: R$ {total:.2f}')

def remProd():
    item = input('Item a ser removido: ')
    try:
        lista_de_produtos.pop(item)
        print('Produto removido.')
    except:
        print('Produto não encontrado.')

lista_de_produtos = {}

while True:
    print('='*20)
    print('ADD PRODUTO [1]')
    print('LISTAR PRODUTS [2]')
    print('REMOVER PRODUTOS [3]')
    print('SAIR [0]')
    print('='*20)
    op = int(input('OPÇÂO: '))
    if op == 0:
        break
    elif op == 1:
        addProd()
    elif op == 2:
        listProd()
    elif op == 3:
        remProd()
    else:
        print('Opção inválida. Tente novamente.')
print('ATÈ MAIS :)')