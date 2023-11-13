"""Create a program that calculates BMI (BMI = W/H*H,
where P is the weight and A is the height.) of a person
and classify the person accordingly with your BMI"""

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
BMI = w/h**2

print(f'Weight: {w}\nHeight: {h}\n')

if BMI < 17:
    print("Very underweight.")
elif 17 <= BMI < 18.5:
    print("Underweight.")
elif 18.5 <= BMI < 25:
    print('Normal weight.')
elif 25 <= BMI < 30:
    print('Overweight.')
elif 30 <= BMI < 35:
    print('Obesity')
elif 35 <= BMI < 40:
    print('Severe obesity.')
elif BMI >= 40:
    print('Morbid obsity.')