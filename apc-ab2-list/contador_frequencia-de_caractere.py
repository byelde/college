string = input()

lista_caractere = {}

for caractere in string:
    lista_caractere[caractere] = string.count(caractere)
lista_caractere = sorted(lista_caractere.items(), reverse=True)

for conjunto in lista_caractere:
    print(f'{conjunto[0]} {conjunto[1]}')