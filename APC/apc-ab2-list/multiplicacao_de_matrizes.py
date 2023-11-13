'''
A primeira linha terá 3 inteiros N, M, O :

- N representa a quantidade de linhas da matriz A.

- M representa a quantidade de colunas da matriz A e a quantidade de linhas da matriz B.

- O indica a quantidade de colunas da matriz B.

Sendo seguido de N linhas com M números inteiros representando a matriz A, logo em seguida mias M linhas com O números indicando a matriz B.

As matrizes A e B são compatíveis na multiplicação.
'''

dimensoes =  input().split()
N = int(dimensoes[0]) #linhas da matriz A.
M = int(dimensoes[1]) #colunas da matriz A e a quantidade de linhas da matriz B.
O = int(dimensoes[2]) #colunas da matriz B
matriz_A = []
matriz_B = []
matriz_C = [[0 for c in range(O)] for c2 in range(N)]

# Input Matriz A
for linha in range(N):
    entradas_linhas = input().split()
    saida_linhas = []
    for valor in entradas_linhas:
        valor = int(valor)
        saida_linhas.append(valor)
    matriz_A.append(saida_linhas)

# Input Matriz B
for linha in range(M):
    entradas_linhas = input().split()
    saida_linhas = []
    for valor in entradas_linhas:
        valor = int(valor)
        saida_linhas.append(valor)
    matriz_B.append(saida_linhas)

# Geração da matriz resultante
for linha in range(N):
    for coluna in range(O):
        soma = 0
        for k in range(M):
            soma += matriz_A[linha][k] * matriz_B[k][coluna]
        matriz_C[linha][coluna] =  str(soma) #STR para a função Join funcionar

# Output matriz resultante
for linha in matriz_C:
    print(' '.join(linha))