'''
Descrição
Faça um programa para corrigir provas de múltipla escolha. Cada prova tem 10 questões, cada questão valendo um ponto. O primeiro conjunto de dados a ser lido é o gabarito para a correção da prova. Depois serão dados os números dos alunos e suas respectivas respostas. O programa encerra a entrada quando o número de um aluno dado for igual a 9999

Formato de entrada
Uma sequência de 10 caracteres correspondendo ao gabarito. Depois é dada uma sequência de números inteiros representando o aluno e a uma sequencia de caracteres correspondendo a sua resposta.

Formato de saída
Para cada aluno lido, na mesma ordem de leitura, deve ser impresso seu número e sua nota. A nota deve ser formatada com uma casa decimal.
Ao final, deve ser impresso a porcentagem de aprovação, sabendo-se que a nota mínima para aprovação é de 6. O percentual deve ser impresso com uma casa decimal seguido do caractere %.
Por fim, deve ser impressa a nota que teve a maior frequência absoluta, ou seja, a nota que apareceu o maior número de vezes (supondo a inexistência de empates).
'''

#=========================================
# Receber id e notas
gab = input()

id_alunos = []
resps_alunos = []

while True:
    id_aluno = int(input())
    if id_aluno == 9999:
        break
    resps_alunos.append(str(input()))
    id_alunos.append(id_aluno)
# calcular notas
nota_aluno = 0
notas = []

for c1 in range(len(resps_alunos)):
    for n,a in enumerate(resps_alunos[c1]):
        if a == gab[n]:
            nota_aluno += 1
    notas.append(nota_aluno)
    nota_aluno = 0
print(notas)

# calcular porcentagem de aprovados
aprovados = 0
for nota in notas:
    if nota >= 6:
        aprovados += 1

p_aprovados = f'{(aprovados/len(id_alunos))*100:.1f}%'

# calcular nota que mais apareceu
nmf, fn = 0, 0
for n, nota in enumerate(notas):
    if notas.count(nota) > fn:
        nmf = nota

# mostrar valores
for c in range(len(id_alunos)):
    print(f'{id_alunos[c]} {notas[c]:.1f}')
print(p_aprovados)
print(f'{nmf:.1f}')