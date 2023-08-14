from os import system
import operations as o
from colored import Fore, Style

while True:
    while True:
        o.menu()
        choice = int(input())
        if not 1 <= choice <= 5:
            system('cls')
            print(f'{Fore.red}Write a valid value{Style.reset}')
        else:
            break
    if choice == 1:
        print(o.soma(int(input('N1: ')),int(input('N2: '))))
    elif choice == 2:
        print(o.sub(int(input('N1: ')),int(input('N2: '))))
    elif choice == 3:
        print(o.mult(int(input('N1: ')),int(input('N2: '))))
    elif choice == 4:
        print(o.div(int(input('N1: ')),int(input('N2: '))))
    elif choice == 5:
        print(o.fact(int(input('N: '))))

    choice2 = input('Do you wanna continue? [Y/N] ').upper()
    if choice2 == 'Y':
        system('cls')
    elif choice2 == 'N':
        print(f'{Fore.green}GOOD BYE{Style.reset}')
        break