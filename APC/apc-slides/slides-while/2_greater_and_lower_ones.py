'''Create a program receive some numbers and show the greater and lower ones'''

#imports
from error import error

#main
numbers = []
while True:
    while True:
        try:
            n = int(input('Number (Press 0 to out): '))
            break
        except:
            error()
    if n == 0:
        break
    numbers.append(n)
try:
    print(f'Greater one: {max(numbers)}')
    print(f'Lower one: {min(numbers)}')
except:
    print('No one value.')