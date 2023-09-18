def Linha():
    print('='*50)

def Aprovacao(media):
    print(f'Aluno(a) aprovado(a) com média {media}')

def Reprovacao(media):
    print(f'Aluno(a) reprovado(a) com média {media}')

# CABEÇALHO
Linha()
print(f'{"STATUS DO DISCENTE":^50}')
Linha()

# INPUT DE NOTAS
notas = []
notas.append(float(input('AB1: ')))
notas.append(float(input('AB2: ')))

for nota in notas:
    if nota < 7:
        Linha()
        print('Nota abaixo de 7,0. Reavalização necessária:')
        notas.append(float(input('Reavaliação: ')))
        break

# CÁLCULO DA MÉDIA
notas.sort()
media = (sum(notas[-2:]))/2

Linha()

# PROCESSAR STATUS
if media >= 7:
    status = 'AP'
    Aprovacao(media)

elif media < 5:
    status = 'RP'
    Reprovacao(media)

elif 7 > media >= 5:
    # NOVAMENTE O CICLO
    print('Média abaixo de 7,0. Reavalização final necessária:')
    nota_final = float(input('Nota final: '))
    mediaF = (6*media + 4*nota_final)/10

    Linha()

    if mediaF >= 5.5:
        status = 'AF'
        Aprovacao(mediaF)
    else:
        status = 'RF'
        Reprovacao(mediaF)

print(f'Status do(a) aluno(a): {status}')