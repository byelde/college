'''Create a program that receives 2 grades of n students and print the averages. Stop when n = -1'''

#imports
from error import error

#main
c = 1
grades = []
while True:
    print(f'{c}º Student')
    n1 = float(input('n1: '))
    if n1 == -1:
        break
    n2 = float(input('n2: '))
    if n2 == -1:
        break
    av = (n1+n2)/2
    grades.append(av)
    c += 1

c = 0
while True:
    try:
        print(f'{c+1}° avereage: {grades[c]}')
        c += 1
        if c == len(grades):
            break
    except:
        print('No one value.')
        break