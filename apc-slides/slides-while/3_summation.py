'''Create a program receive some numbers and show the summation between them'''

#imports
from error import error

#main
summ = 0
while True:
    while True:
        try:
            n = int(input('Number (Press 0 to out): '))
            break
        except:
            error()
    if n == 0:
        break
    summ += n
try:
    print(f'Summation: {summ}')
except:
    print('No one value.')