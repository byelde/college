'''Create a program to print the even numbers between 2-M (M is a number chosen by user)'''

from error import error
from os import system

while True:
    try:
        M = int(input('Number: '))
        break
    except:
        error()

system('cls')

for n in range(2,M+1):
    if n % 2 == 0:
        print(n)