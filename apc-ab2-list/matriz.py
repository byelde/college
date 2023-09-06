#========================================
# Receber inputs

# dimensoes
dimensoes = input('dimensoes: ')
dl, dc = int(dimensoes[0]), int(dimensoes[2])

valores = []
matriz_t = []

#valores
for linha in range(dl):
    valores.append(input('valores: ').split())

print(valores)
'''[['1', '2', '3'], ['4', '5', '6']]'''
#========================================
# for linha in range(len(valores)):
#     # print(" ".join(valores[linha]))
#     for coluna in range(len(valores[linha])):
#         matriz_t[f'{coluna},{linha}'] = valores[linha][coluna]
# print(matriz_t)