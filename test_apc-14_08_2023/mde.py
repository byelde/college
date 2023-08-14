n = int(input('Digite um número: '))
n2  = int(input('Digite outro número: '))

if n > n2:
    menorn = n2
elif n2 > n:
    menorn = n
else: 
    menorn = n

maiordiv = 1

for c in range(1,menorn+1): 
    if (n % c == 0) and (n2% c == 0):
        maiordiv = c

print(maiordiv)