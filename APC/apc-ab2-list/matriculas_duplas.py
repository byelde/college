# IMPUTS
p2 = []
p3 = []
matdupla = []

p2 = input().split()
p3 = input().split()

# CHECAR MAT DUPLA
for aluno in p2:
    if aluno in p3:
        matdupla.append(aluno)

for aluno in matdupla:
    print(f'{aluno}', end=' ')