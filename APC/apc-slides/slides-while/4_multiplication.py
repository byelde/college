'''Create a program receive some numbers and show the multiplication between them'''

#imports
from error import error

#main
m = 1
sm = False
while True:
    while True:
        try:
            n = int(input('Number (Press 0 to out): '))
            sm = True
            break
        except:
            error()
    if n == 0:
        break
    m *= n

if sm:
    m = 0

try:
    print(f'Multiplication between them: {m}')
except:
    print('No one value.')