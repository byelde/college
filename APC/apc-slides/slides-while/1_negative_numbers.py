'''Create a program receive some numbers and show how much of them are negatives.'''

#imports
from error import error

#main
non = 0
while True:
    while True:
        try:
            n = int(input('Number (Press 0 to out): '))
            break
        except:
            error()
    if n < 0:
        non += 1
    elif n == 0:
        break

print(f'How much negatives ones: {non}')