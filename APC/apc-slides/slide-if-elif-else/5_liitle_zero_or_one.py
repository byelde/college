"""Create a program determine is there is a winner in a match of 'little zero or one'."""


#imports
from colored import Fore, Style
from os import system
from error import error

#main
while True:
    player1 = int(input('Player N°1: '))
    if player1 == 1 or player1 == 0:
        break
    else:
        error()

while True:
    player2 = int(input('Player N°2: '))
    if player2 == 1 or player2 == 0:
        break
    else:
        error()

while True:
    player3 = int(input('Player N°3: '))
    if player3 == 1 or player3 == 0:
        break
    else:
        error()

system('cls')

print(f'\nMoves:\nPlayer N°1: {player1}\nPlayer N°2: {player2}\nPlayer N°3: {player3}\n')

if player1 != player2 == player3:
    print("Player N°1 won")
elif player2 != player1 == player3:
    print('Player N°2 won')
elif player3 != player1 == player2:
    print('Player N°3 won')
else:
    print(f'{Fore.green}A tie.{Style.reset}')