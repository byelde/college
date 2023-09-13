def acumulador():
    valor = int(input())
    if valor == 0:
        return 0
    acumulador()
    print(valor)

acumulador()