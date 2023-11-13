'''Create a program receives an integer and display its factorial'''

#imports
from error import error

#main
while True:
    try:
        n = int(input('n: '))
        break
    except:
        error()

m = 1
for c in range (n,0,-1):
    m *= c

print(m)