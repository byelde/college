"""Create a program that receive a integer N (1 <= N <= 12) and print the corresponding name of the month."""


#imports
from os import system
from time import sleep
from colored import Fore, Back, Style

#main
months_names = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"Dezember"}

while True:
    try:
        n = int(input("Month: "))
        if 1 <= n <= 12:
            print(months_names[n])
            break
        else:
            print('Invalid month.')
    except:
        system('cls')
        print(f"{Fore.red}ERROR. Write a valid number.{Style.reset}")
        sleep(0.3)