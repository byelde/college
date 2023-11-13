'''Create a program receives 10 ages and print the max one and min one'''

#imports
from error import error

#main
lista = []
for c in range(1,11):
    while True:
        try:
            n = int(input(f'{c}º Age: '))
            lista.append(n)
            break
        except:
            error()
    

print(f'Max age: Age N°{lista.index(max(lista))+1} - {max(lista)}')
print(f'Minimum age: Age N°{lista.index(min(lista))+1} - {min(lista)}')