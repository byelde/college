"""Create a program input a age (integer) of a person
a inform your voter class"""

#imports
from error import error
from os import system
from colored import Fore, Style

#main
while True:
    try:
        age = int(input('Age: '))
        if not age <= 0:
            break
        else:
            error()
    except:
        error()

system('cls')
print(f'Age: {age}')

if age < 16:
    print(f'{Fore.red}Non-voter.{Style.reset}')
elif 16 <= age < 18 or age > 65:
    print(f'{Fore.yellow}Optional voter.{Style.reset}')
else:
    print(f'{Fore.green}Mandatory voter.{Style.reset}')
