dimensoes = input('Digite as dimensoes da matriz:\n').split()
l, c = int(dimensoes[0]), int(dimensoes[1])

matriz = []
matriz_t = [[0 for coluna in range(l)] for linha in range(c)]

print('Digite os elementos da matriz:')
for linha in range(l):
    linha = input().split()
    matriz.append(linha)


for linha in range(l):
    for coluna in range(c):
        matriz_t[coluna][linha] = matriz[linha][coluna]

print('Matriz transposta:')
for linha in matriz_t:
    for valor in linha:
        print(f'{valor:<6}', end='')
    print()