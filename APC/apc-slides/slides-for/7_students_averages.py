'''Create a program that receives 2 grades of 5 students and print the averages.'''

#imports
from error import error

#main
grades = []
while True:
    try:
        for c in range(0,5):
            print(f'{c+1}° Student:')
            n1 = float(input('1º grade: '))
            n2 = float(input('2º grade: '))
            m = (n1+n2)/2
            grades.append(m)
            print()
        break
    except:
        error()
    
for c in range(0,5):
    print(f'{c+1}° student average: {grades[c]}')