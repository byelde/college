"""create a program receive three values and inform if is possible form a triangle and wich is it`s type"""

#iports
from error import error
from os import system

#main
while True:
    try:
        s1 = float(input('Side 1: '))
        if not s1 <= 0:
            break
        else:
            error()
    except:
        error()

while True:
    try:
        s2 = float(input('Side 2: '))
        if not s2 <= 0:
            break
        else:
            error()
    except:
        error()

while True:
    try:
        s3 = float(input('Side 3: '))
        if not s3 <= 0:
            break
        else:
            error()
    except:
        error()

system('cls')
print(f'\nSides:\nS1: {s1}\nS2: {s2}\nS3: {s3}\n')

if s1 < (s2+s3) or s2 < (s1+s3) or s3 < (s1+s2):
    if s1 == s2 == s3 == s1:
        print('Equilateral triangle.')
    elif s1 > s2 > s3 or s3 > s2 > s1:
        print('Scalene triangle.')
    else:
        print('Isosceles triangle.')
else:
    print('Not triangle')