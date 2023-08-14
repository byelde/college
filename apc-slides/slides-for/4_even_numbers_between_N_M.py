'''Create a program to print the even numbers between N-M (N and M are numbers chosen by user)'''

from error import error
from os import system

while True:
    try:
        N = int(input('Number 1: '))
        break
    except:
        error()

while True:
    try:
        M = int(input('Number 2: '))
        break
    except:
        error()

system('cls')

print(f'Number 1: {N} and Number 2: {M}')
for n in range(N,M+1):
    if n % 2 == 0:
        print(n)