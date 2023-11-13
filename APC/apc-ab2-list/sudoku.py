def valSudoku(sudoku):
    # Declarações
    referencia = [n for n in range(1,10)]
    validade = True

    # Análise das linhas
    for linha in sudoku:
        if (sorted(linha) != referencia):
            validade = False

    # Análise das colunas
    for linha in range(9):
        sudoku_t = []
        for coluna in range(9):
            sudoku_t.append(sudoku[coluna][linha])
        if (sorted(sudoku_t) != referencia):
            validade = False
    
    # Aálise dos quadrados
    for linha in range(9):
        for coluna in range(9):
            # PONTOS INICIAIS DE CADA QUADRADO
            if (linha == 0 or linha % 3 == 0) and (coluna == 0 or coluna % 3 == 0):
                quadrado = []
                for aux in range(3):
                                                       #DE C ATE C+3
                    quadrado.extend(sudoku[linha+aux][coluna:coluna+3])
                if (sorted(quadrado) != referencia):
                    validade = False

    if validade:
        return 'SIM'
    else:
        return 'NAO'

qntd_instancias =  int(input())
for nI in range(qntd_instancias):
    matriz = []
    for c in range(9):
                 # TRANSFORMAR CADA VALOR DA LISTA (INPUT SPLITADO)
        linha = [int(valor) for valor in input().split()]
        matriz.append(linha)
    print(f'Instancia {nI+1}\n{valSudoku(matriz)}\n')