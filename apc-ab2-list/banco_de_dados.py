"""A empresa WOOF está entrando no mercado das redes sociais. Só que ela precisa de um banco de dados para armazenar os dados dos seus usuários.
O dono da empresa é muito amigo seu, e sabe que você é um ótimo programador, logo, te chamou para implementar esse banco de dados.
As informações dos usuários que você deve guardar são:

Idade.
Nome.
Sexo.
Estado civil.
Quantidade de amigos.
Quantidade de fotos.

Formato de entrada
Você vai receber os dados do usuário:
Um inteiro, representando a quantidade de usuários a serem adicionados ao banco de dados.
Um inteiro, contendo a idade.
Uma string, de até 50 caracteres, contendo o nome.
Um caractere, sendo ele M ou F, que é o sexo.
Uma caractere, simbolizando o estado cívil: S - Solteiro, C - Casado. N - Namorando. D - Divorciado.
Um inteiro, representando o número de amigos.
Um inteiro, representando a quantidade de fotos que estão no perfil.

Formato de saída
Imprimir as informações de todos os usuários, na sequencia em que eles foram adicionados, uma por linha.
Deve haver uma quebra de linha entre os casos de testes e ao fim do programa."""


# receber inputs
quantidade = int(input())
idades = []
nomes = []
sexo = []
est_civil = []
qnt_amigos = []
qnt_fotos = []


for c in range(quantidade):
    idades.append(int(input()))
    nomes.append(input())
    sexo.append((input()))
    est_civil.append((input()))
    qnt_amigos.append(int(input()))
    qnt_fotos.append(int(input()))
    

# dados
for c in range(quantidade):
    print(f'Idade: {idades[c]}')
    print(f'Nome: {nomes[c]}')
    print(f'sexo: : {sexo[c]}')
    print(f'Vida: {est_civil[c]}')
    print(f'Ataque: {qnt_amigos[c]}')
    print(f'Defesa: {qnt_fotos[c]}')
