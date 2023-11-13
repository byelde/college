crip= {'0':'6',
       '1':'7',
       '2':'9',
       '3':'8',
       '4':'A',
       '5':'2',
       '6':'B',
       '7':'F',
       '8':'1',
       '9':'C',
       'A':'0',
       'B':'D',
       'C':'E',
       'D':'3',
       'E':'5',
       'F':'4'}

qntd_senhas = int(input())
senhas = []
senhas_crip = []
caracteres_totais = 0


try:
    for senha in range(qntd_senhas):
        senha_digitada = input()
        senhas.append(senha_digitada)

    for senha in senhas:
        senha_alt = []
        for caractere in senha:
            caracteres_totais += 1
            if caractere in crip.keys():
                senha_alt.append(crip[caractere])
            elif caractere.isupper():
                senha_alt.append(caractere)
            else:
                senhas.append()
        senhas_crip.append(''.join(senha_alt))

    for senha in senhas_crip:
        print(f'-{senha}',end='')
    print(f' {caracteres_totais}')

except:
    print('Alguma senha eh invalida!')
