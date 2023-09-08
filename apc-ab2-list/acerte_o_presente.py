#==============================
# Inputs
qntd_pessoas = int(input())

pessoas = {}

for pessoa in range(qntd_pessoas):
    dados_pessoa = input().split()
    pessoas[dados_pessoa[0]] = dados_pessoa[1:]

while True:
    tentativa = input().split()
    if 'FIM' in tentativa:
        break
    if tentativa[1] in pessoas[tentativa[0]]:
        print('Uhul! Seu amigo secreto vai adorar')
    else:
        print('Tente Novamente!')