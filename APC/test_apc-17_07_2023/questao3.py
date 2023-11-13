n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
n3 = float(input('3° nota: '))

media = (n1+n2+n3)/3
print(f'A média entre elas é {media:.3f}')

mediap1 = ((n1*2)+(n2*2)+(n3*3))/(2+2+3)
print(f'A média ponderada entre elas é {mediap1:.3f}')

mediap2 = ((n1*1)+(n2*2)+(n3*2))/(1+2+2)
print(f'A média ponderada entre elas é {mediap2:.3f}')
