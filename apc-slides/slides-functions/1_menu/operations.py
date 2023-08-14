def soma(a,b):
    s = a + b
    return s

def sub(a,b):
    s = a - b
    return s

def mult(a,b):
    m = a*b
    return m

def div(a,b):
    d = a/b
    return d

def fact(b):
    f = 1
    for c in range(b,0,-1):
        f *= c
    return f

def menu():
    print('-='*15)
    print('[1] Sum')
    print('[2] subtraction')
    print('[3] Multiplication')
    print('[4] Division')
    print('[5] Factorial')
    print('-='*15)