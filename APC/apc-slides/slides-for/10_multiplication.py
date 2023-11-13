'''Create a program receives 10 values and print the multiplications between them'''

#imports
from error import error

#main
m = 1
for c in range(0,10):
    while True:
        try:
            n = int(input(f'n{c+1}: '))
            break
        except:
            error()
    m *= n

print(m)