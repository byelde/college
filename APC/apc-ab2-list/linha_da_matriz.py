linha = int(input())
operação = input()

matriz = []
for row in range(12):
    matriz_row = input().split()
    for id,number in enumerate(matriz_row):
        matriz_row[id] = int(matriz_row[id])
    matriz.append(matriz_row)

if operação == 'S':
    print(f'{sum(matriz[linha]):.1f}')

elif operação == 'M':
    print(f'{sum(matriz[linha])/len(matriz[linha]):.1f}')
    