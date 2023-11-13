#imports
from os import system
from time import sleep
from colored import Fore, Style

#functions
def error():
    system('cls')
    print(f'{Fore.red}ERROR. Write a valid value.{Style.reset}')
    sleep(0.3)