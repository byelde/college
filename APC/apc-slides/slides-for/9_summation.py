'''Create a program receives 10 values and print the summation of them.'''

#imports
from error import error

#main
s = 0
while True:
    try:
        for c in range(0,10):
            n = int(input(f'n{c+1}: '))
            s += n
        break
    except:
        error()

print(f'The summation of this values is: {s}')