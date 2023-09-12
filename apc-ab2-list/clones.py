'''
A entrada contém vários blocos de casos de testes.
Cada caso começa com uma linha contendo dois inteiros:
O número 1<=n<=20000 pessoas.
O tamanho 1<=m<=20 de sequências de DNAs.

As próximas n linhas contém as sequencias de DNAs.
Cada linha contem uma sequencia de m caracteres onde cada caractere é A, C, G ou T.

A entrada termina por um bloco onde n=m=0.
'''

conjunto_de_dados = []

while True:
    qntd_p_s = input().split()
    qntd_pessoas =  int(qntd_p_s[0])
    qntd_genes = int(qntd_p_s[1])
    if qntd_pessoas == 0 and qntd_genes == 0:
        break

    dados1 = {}
    for c in range(qntd_pessoas):
        sequencia_dna = input()
        if sequencia_dna in dados1.keys():
            dados1[sequencia_dna] += 1
        else:
            dados1[sequencia_dna] = 0

    dados2 = []
    dados2.append(qntd_pessoas)
    for chave, valor in dados1.items():
        dados2.append(valor)
    
    conjunto_de_dados.append(dados2)

for dados in conjunto_de_dados:
    p_analise = dados[1:]
    # print(dados)
    for c in range(dados[0]):
        print(p_analise.count(c))
