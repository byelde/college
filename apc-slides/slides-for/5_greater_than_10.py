from error import error

lista = []

for c in range(1,11):
    while True:
        try:
            n = int(input(f"Number[{c}]: "))
            lista.append(n)
            break
        except:
            error()
print(sorted(lista))
print(f'Max value: {max(lista)}')