'''
Você deverá imprimir a matriz resultante no formato de matriz, onde os elementos da primeira linha aparecerão lado a lado, separados por um espaço (não deverá haver um espaço depois do último elemento de cada linha), a soma da sua diagonal principal e secundária e os elementos menores e maiores que zero.

OBS.: Cada linha da matriz será separada por um final de linha, inclusive depois da última. Além disso se a matriz dada não for quadrada você não poderá determinar as somas da sua diagonal principal e secundária. Verifique os exemplos!!
'''

#=======================================
# Inputs
dimensoes = input().split()
l = dimensoes[0]
c = dimensoes[1]

matriz = []
linha_matriz = []

for linha in range(int(l)*int(c)):
    valor = int(input())
    linha_matriz.append(valor)
    if (linha+1)%int(c) == 0:
        matriz.append(linha_matriz)
        linha_matriz = []

#========================================
# Processamento

# diagonal principal e secundária
if c != l:
    pass

else:
    # Somar Principal
    dia_P = 0
    for nL, linha in enumerate(matriz):
        for nC,valor in enumerate(linha):
            if nC == nL:
                dia_P += valor

    # Somar Secundária
    dia_S = 0
    id_S = int(c)-1
    for nL, linha in enumerate(matriz):
        for nC, valor in enumerate(linha):
            if nC == id_S:
                dia_S += valor
                id_S -= 1

# valores menores que 0
num_ME = 0

for linha in matriz:
    for valor in linha:
        if valor < 0:
            num_ME += 1

# valores maiores que 0
num_MA = 0

for linha in matriz:
    for valor in linha:
        if valor > 0:
            num_MA += 1

#========================================
# Output

print('Matriz formada:')
for linha in matriz:
    print(' '.join(map(str,linha)))

if c != l:
    print('A diagonal principal e secundaria nao pode ser obtida.')
else:
    print(f'A diagonal principal e secundaria tem valor(es) {dia_P} e {dia_S} respectivamente.')

print(f'A matriz possui {num_ME} numero(s) menor(es) que zero.')
print(f'A matriz possui {num_MA} numero(s) maior(es) que zero.')
