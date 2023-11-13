valor = int(input('VAlor a ser sacado R$'))

# 100 reais
c100 = valor//100
valor -= c100*100
print(f'{c100} nota(s) de R$100,00')

# 50 reais
c50 = valor //50
valor -= c50*50
print(f'{c50} nota(s) de R$50,00')

# 20 reais
c20 = valor // 20
valor -= c20*20
print(f'{c20} nota(s) de R$20,00')

# 10 reais
c10 = valor//10
valor -= c10*10
print(f'{c10} nota(s) de R$10,00')

#5 reais
c5 = valor//5
valor -= c5*5
print(f'{c5} nota(s) de R$5,00')

# 2 reais
c2 = valor//2
valor -= c2*2
print(f'{c2} nota(s) de R$2,00')

#1 real
c1 = valor
print(f'{c1} nota(s) de R$1,00')