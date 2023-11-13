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

ids_resps = []

ids = []
resps = []
while True:
    id_r = input().split()
    if id_r[0] == '9999':
        break
    ids.append(int(id_r[0]))
    resps.append(id_r[1])

# calcular notas
notas = []

for resposta in resps:
    nota_aluno = 0
    for n in range(10):
        if resposta[n] == gab[n]:
            nota_aluno += 1
    notas.append(nota_aluno)


# calcular porcentagem de aprovados
aprovados = 0
for nota in notas:
    if nota >= 6:
        aprovados += 1
p_aprovados = f'{(aprovados/len(ids))*100:.1f}%'


# calcular nota que mais apareceu
n_m_f, maior_f = 0, -1
for nota in notas:
    if notas.count(nota) > maior_f:
        maior_f = notas.count(nota)
        n_m_f = nota


# mostrar valores
for c in range(len(ids)):
     print(f'{ids[c]} {notas[c]:.1f}')
print(p_aprovados)
print(f'{n_m_f:.1f}')