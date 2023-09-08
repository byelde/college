qntd_livros = int(input())

lista_livros = []
for num in range(qntd_livros):
    lista_livros.append(input())

livro_procurado = input()

if livro_procurado in lista_livros:
    print('Sim')
else:
    print('Não')