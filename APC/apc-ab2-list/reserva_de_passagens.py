'''
Uma sequência de 37 pares de inteiros, indicando o número do voo e a quantidade de lugares disponíveis no respectivo voo. Depois você lerá uma sequência de pedidos de reserva. Cada pedido de reserva é representado por um par de inteiros indicando, respectivamente, o número do documento de identidade do cliente e o número do voo que o cliente deseja viajar. A entrada se encerra quando o número do documento de identidade do cliente for igual a 9999. Existe a possibilidade de que o cliente deseje viajar em um voo que não está sendo oferecido pela Ambrosino Airlines.
'''
voos = {}

for contador in range(37):
    dados_voo = input().split()
    voos[dados_voo[0]] = int(dados_voo[1])

dados_clientes = {}
while True:
    dado_cliente = input().split()
    if dado_cliente[0] == '9999':
        break
    dados_clientes[dado_cliente[0]] = dado_cliente[1]
    
for id, voo in dados_clientes.items():
    try:
        if voos[voo] > 0:
            voos[voo] -= 1
            print(id)
        else:
            print('INDISPONIVEL')
    except:
            print('INDISPONIVEL')

    # print(id, voo, voos[voo])