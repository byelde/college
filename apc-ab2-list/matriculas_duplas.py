# IMPUTS
p2 = []
p3 = []
matdupla = []

for c in range(45):
    p2.append(int(input()))

for c in range(30):
    p3.append(int(input()))

# CHECAR MAT DUPLA
for aluno in p2:
    if aluno in p3:
        matdupla.append(aluno)

for aluno in matdupla:
    print(f'{aluno}', end=' ')