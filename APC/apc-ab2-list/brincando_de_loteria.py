'''
Um grupo de amigos se reuniu para brincar de loteria. Cada amigo podia apostar em até 10 números diferentes (entre 1 e 100). Depois de todos apostarem, eram sorteados os números. Com base nas apostas e nos números sorteados, o objetivo era calcular o número de acertos de cada um e imprimir o resultado ordenado de forma crescente pelo número de acertos. Havendo empate, a ordem era definida pelo nome.

O programa deve ler um número qualquer de apostas, sendo uma por linha. Cada linha é formada pelo primeiro nome do apostador, de um espaço em branco e de uma sequência de números (entre 1 e 100) separados entre si por um espaço em branco. Chega-se ao fim da leitura das apostas quando se encontra uma linha com a string FIM.Depois de concluída a leitura das apostas, deve ser lido o resultado do sorteio, que pode ter de 1 a 10 números (com valores entre 1 e 100) separados entre si por um hifens.

A saída consiste de uma relação de apostadores e seus acertos, sendo que o número acertos é representado pelo uso do caractere '+' (por exemplo, para 3 acertos seria +++). A relação deve ser ordenada de forma crescente pelo número de acertos. Em caso de empate, define-se a ordem pelo nome dos apostadores.
'''

# Ler os inputs (nome e tentativas de acerto) X
# Criar uma variável para guardar esses valores X
# Guardar nomes e tentativas separados X
# Recolher resultado

#==============================================
cartelas_de_cada = {}

# Dados
while True:
    dados = input().split()
    if 'FIM' in dados:
        break
    cartelas_de_cada[dados[0]] = dados[1:]

resultado = input().split(sep='-')


# CAlcular quantos acertos cada um teve
# Ver se cada tentativa esta detro do resultado
acertos_de_cada = {}

for nome, tentativas in cartelas_de_cada.items():
    for tentativa in tentativas:
        if tentativa in resultado:
            try:
                acertos_de_cada[nome] += 1
            except:
                acertos_de_cada[nome] = 1
        else:
            try:
                acertos_de_cada[nome] += 0
            except:
                acertos_de_cada[nome] = 0


#Printar em ordem decrestente de valores e depois por nome
ordem = []

for c in range(max(acertos_de_cada.values())+1):
    lista_por_qntd_acertos = []
    for dado in acertos_de_cada.items():
        if dado[1] == c:
            lista_por_qntd_acertos.append(dado)
    lista_por_qntd_acertos = sorted(lista_por_qntd_acertos)
    ordem.append(lista_por_qntd_acertos)


for linha in ordem:
    for dados in linha:
        print(f'{dados[0]} {"+"*dados[1]}')