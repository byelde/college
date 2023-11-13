"""Create a program receives two integer, the first one corresponding to a month and the second one to a year, and inform how much day the month has."""

#imports
from os import system
from time import sleep
from colored import Fore, Style

#functions
def error():
    system('cls')
    print(f'{Fore.red}ERROR. Write a valid value.{Style.reset}')
    sleep(0.3)

#main
while True:
    try:
        month = int(input("Month: "))
        if 1 <= month <= 12:
            break
        else:
            error()
    except:
        error()

while True:
    try:
        year = int(input("Year: "))
        break
    except:
        error()

months_days = {1:31, 2:28, 3:31, 4:30, 5:31,6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    months_days[2] += 1

system('cls')

print(f'Data: Month = {month} and Year = {year}')
print(f'{Fore.green}The month {month} has {months_days[month]} days.{Style.reset}')