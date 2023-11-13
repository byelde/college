"""Create a program input a age (integer) of a person
a inform your voter class"""

#imports
from error import error
from os import system
from colored import Fore, Style
from voter_class import voter

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

print(f'Class: {voter(age)}')
