'''
Escreva umprograma que leia uma matriz 3 x 3 de inteiros da entrada padrão e calcule a média de todos seus valores, o maior valor lido , o valor delta e a soma dos elementos da diagonal princial.
O delta é igual a 1 se o maior valor for positivo, -1 se for negativo e zero se for zero.
'''

#================================
# Inputs

matriz = []
linha_matriz = []

for c in range(9):
    valor = int(input())
    linha_matriz.append(valor)
    if (c+1)%3==0:
        matriz.append(linha_matriz)
        linha_matriz = []

#=================================
# Processamento

# Média todos os valores
# Maior valor lido
# Soma diagonal principal
# Delta

somatorio = []
soma_dia_p = 0

for nL, linha in enumerate(matriz):
    for nC, valor in enumerate(linha):
        somatorio.append(valor)
        if nL ==  nC:
            soma_dia_p += valor

media = sum(somatorio)/ len(somatorio)
maior_valor = max(somatorio)
if maior_valor > 0:
    delta = 1
elif maior_valor < 0:
    delta = -1
else:
    delta = 0

#=================================
# Output

print(f'{media:.2f} {maior_valor} {delta} {soma_dia_p}')
