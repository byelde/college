'''Descrição
Você está fazendo o banco de dados do seu projeto de P1, que será um jogo, que vai conter informações de inúmeros monstros e personagens, mas não possui nenhum conhecimento de SQL, logo, precisará aproveitar algum recurso da linguagem C para fazer o banco de dados.

Formato de entrada
Um inteiro X, representando a quantidade de personagens/monstros que constarão no banco.
Os dados a serem colocados no banco:
Uma sequencia de caracteres, que poderá ter no máximo 20 caracteres, representando um nome.
5 inteiros, representando ID, Level, Vida, Ataque e Defesa.

Formato de saída
Uma impressão do seu banco de dados, com os dados organizados como o modelo de saida.'''

# receber inputs
quantidade = int(input())
ids = []
levels = []
vidas = []
ataques = []
defesas = []
nomes = []

for c in range(quantidade):
    nomes.append(input())
    ids.append(int(input()))
    levels.append(int(input()))
    vidas.append(int(input()))
    ataques.append(int(input()))
    defesas.append(int(input()))

# dados
for c in range(quantidade):
    print(f'Nome: {nomes[c]}')
    print(f'ID: {ids[c]}')
    print(f'Level: {levels[c]}')
    print(f'Vida: {vidas[c]}')
    print(f'Ataque: {ataques[c]}')
    print(f'Defesa: {defesas[c]}')
