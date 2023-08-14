'''Create a program receives 10 numbers and print how much are negatives'''

#imports
from error import error

#main
neg = 0
while True:
    try:
        for c in range(0,10):
            n = int(input(f'{c+1}º number: '))
            if n < 0:
                neg += 1
        break
    except:
        error()

print(f'How much negatives ones: {neg}')