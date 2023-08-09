#iports
from error import error
from os import system

#main
while True:
    try:
        w = float(input('Weight(kg): '))
        if not w <= 0:
            break
        else:
            error()
    except:
        error()

while True:
    try:
        h = float(input('Height(m): '))
        if not h <= 0:
            break
        else:
            error()
    except:
        error()

system('cls')
CMI = w/h**2

print(f'Weight: {w}\nHeight: {h}\n')

if CMI < 17:
    print("Very underweight.")
elif 17 <= CMI < 18.5:
    print("Underweight.")
elif 18.5 <= CMI < 25:
    print('Normal weight.')
elif 25 <= CMI < 30:
    print('Overweight.')
elif 30 <= CMI < 35:
    print('Obesity')
elif 35 <= CMI < 40:
    print('Severe obesity.')
elif CMI >= 40:
    print('Morbid obsity.')