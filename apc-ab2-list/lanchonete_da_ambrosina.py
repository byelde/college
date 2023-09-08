#=================================
# Inpuuts

lista_prod_cad = {}

# Quantidade de produtos para cadastrar
qntd_prod_cad = int(input())

# Cadastro de cada produto
for produto in range(qntd_prod_cad):
    led_produto = int(input())
    descricao_produto = input()
    preco_produto = float(input())
    lista_prod_cad[led_produto] = preco_produto

# Ler pedidos (para quando id_pedido == 0)
lista_prod_pedido = {}
while True:
    led_pedido = int(input())
    if led_pedido == 0:
        break
    qntd_prod_pedido = int(input())
    lista_prod_pedido[led_pedido] = qntd_prod_pedido
#================================
# Processamento

# Calcular valor final
# Escolher produto e adicionar seu preço ao valor final
# obs: desconsiderar produto se produto não cadastrado ou quantidade negativa
valor_final = 0
for produto in lista_prod_pedido.items():
    if produto[0] not in lista_prod_cad.keys() or produto[1] < 0:
        pass
    else:
        valor_final += lista_prod_cad[produto[0]]*produto[1]

#==============================
# Mostrar Valor (valor final)
print(f'{valor_final:.2f}')