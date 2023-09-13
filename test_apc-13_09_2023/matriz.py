def soma(A,B):
    matriz_result = []
    for linha in range(qntd_linha):
        linha_r = []
        for coluna in range(qntd_colunas):
            linha_r.append(str(mA[linha][coluna]+ mB[linha][coluna]))
        matriz_result.append(linha_r)

    for linha in matriz_result:
        print(f"|{' '.join(linha)}|")

def sub(A,B):
    matriz_result = []
    for linha in range(qntd_linha):
        linha_r = []
        for coluna in range(qntd_colunas):
            linha_r.append(str(mA[linha][coluna]- mB[linha][coluna]))
        matriz_result.append(linha_r)

    for linha in matriz_result:
        print(f"|{' '.join(linha)}|")

def inputs():
    global mA
    global mB
    global qntd_colunas
    global qntd_linha

    mA.clear()
    mB.clear()

    print('='*40)
    qntd_linha = int(input('Quantidade de linhas das matrizes: '))
    qntd_colunas = int(input('Quantidade de colunas das matrizes: '))
    for c in range(qntd_linha):
        linha_a = [int(n) for n in input('Linha de A: ').split()]
        mA.append(linha_a)
    for c in range(qntd_linha):
        linha_b = [int(n) for n in input('Linha de B: ').split()]
        mB.append(linha_b)

mA = []
mB = []
qntd_linha = 0
qntd_colunas = 0

op = 3
while True:
    if op == 0:
        break
    elif op == 1:
        soma(mA,mB)
    elif op == 2:
        sub(mA,mB)
    elif op==3:
        inputs()
    else:
        print('Valor inválido.')
    print('='*20)
    print('SOMA [1]\nSUBTRAÇÂO[2]\nNOVAS MATRIZES[3]\nSAIR[0]')
    op = int(input())
print('Leva em consideração o menu por favor :)')
    






