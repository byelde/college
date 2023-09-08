import numpy as np

#===================================
# Inputs
qntd = int(input())

list_sudokus = []
for sk in range(qntd):
    sudokuN = []
    for linha_skN in range(9):
        # linha = input()
        linha = '1 2 3 4 5 6 7 8 9'
        sudokuN.append(linha.split())
    list_sudokus.append(sudokuN)

#===================================
# Checar linhas de cada sudoku maior

validade_sdkS = []

for N_sdk in range(qntd):
    validade_sdk = []
    for linha in list_sudokus[N_sdk]:
        for posicao in linha:
            if linha.count(posicao) > 1:
                validade_sdk.append(False)
            else:
                validade_sdk.append(True)

    if False in validade_sdk:
        validade_sdkS.append(False)
    else:
        validade_sdkS.append(True)

#===================================
# Checar colunas do sudoku maior

# sudokus em colunas
list_sudokus_col = []
sudoku_col = []
#escolher qual sudoku vai analisar
for n in range(qntd):
    #escolher a coluna
    for c in range(9):
        coluna = []
        # escolher a coluna em cada linha
        for linha in list_sudokus[n]:
            # adicionar o elemento na coluna
            coluna.append(linha[c])
        # adicionar coluna no sudoku
        sudoku_col.append(coluna)
    # adicionar sudoku na lsta de sudokus
    list_sudokus_col.append(sudoku_col)

validade_sdkS = []


for N_sdk in range(qntd):
    validade_sdk = []
    for linha in list_sudokus_col[N_sdk]:
        for posicao in linha:
            if linha.count(posicao) > 1:
                validade_sdk.append(False)
            else:
                validade_sdk.append(True)

for N_sdk in range(qntd):
    if False in validade_sdk:
        validade_sdkS[N_sdk] = False
    else:
        if validade_sdkS[N_sdk] == False:
            pass
        else:
            validade_sdkS[N_sdk] = True
            