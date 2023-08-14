"""Create a program receives a integer corresponding to a year and inform if it`s leap"""

#imports
from os import system
from time import sleep
from colored import Fore, Back, Style

#main
while True:
    try:
        year = int(input("Year: "))
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
        break
    except:
        system('cls')
        print(f'{Fore.red}ERROR! Write a valid year.{Style.reset}')
        sleep(0.3)