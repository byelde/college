
#====================================
# Inputs
dimensao = int(input())

matriz = []
for c in range(dimensao):
    matriz.append(input().split())

for linha in matriz:
    for n,valor in enumerate(linha):
        linha[n] = int(linha[n])

#====================================
# Processamento 

# Soma das linhas iguais
soma_linhas = []
for linha in matriz:
    soma_linhas.append(sum(linha))

if max(soma_linhas) == min(soma_linhas):
    linhas_iguais = True
else:
    linhas_iguais = False

# soma colunas iguais
soma_colunas = {}

for nL, linha in enumerate(matriz):
    for nC, valor in enumerate(linha):
        try:
            soma_colunas[nC] += valor
        except:
            soma_colunas[nC] = valor

if max(soma_colunas.values()) == min(soma_colunas.values()):
    colunas_iguais = True
else:
    colunas_iguais = False

# Soma diagonais iguais
# Principal
soma_diag_P = 0
for nL, linha in enumerate(matriz):
    for nC, valor in enumerate(linha):
        if nC == nL:
            soma_diag_P += valor

# secundária
soma_diag_S = 0
id_coluna = dimensao-1
for nL, linha in enumerate(matriz):
    for nC, valor in enumerate(linha):
            if id_coluna == nC:
                soma_diag_S += valor
                id_coluna -= 1

if soma_diag_P == soma_diag_S:
    diagonais_iguais = True
else:
    diagonais_iguais = False

#====================================
# Output
if linhas_iguais and colunas_iguais and diagonais_iguais:
    print(soma_diag_P)
else:
    print(-1)