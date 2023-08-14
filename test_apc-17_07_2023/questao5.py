valor_prod = float(input('Valor do  produto: '))
vdesc = valor_prod*0.9
print(f'Valor com 10% de desconto: R${vdesc:.2f}')

print(f'O valor de cada uma das três parcelas será em caso de parcelamento R${valor_prod/3:.2f}')

print(f'A comissão do vendedor a vista R${vdesc*0.05:.2f}')

print(f'A comissão do vendedor a prazo: R${valor_prod*0.05:.2f}')