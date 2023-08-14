'''Create a program that print the Fibonacci Sequence'''

#imports
from error import error

#main
n1 = 0
n2 = 1
while True:
    try:
        v = int(input())
    except:
        error()
    if v == 1:
        print(0)
    elif v <=0:
        error()
    else:
        for c in range(0,v):
            print(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
    break