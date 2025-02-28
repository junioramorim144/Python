valor = float (input ('Digite sua renda mensal para saber seu aumento:'))
aumento = valor + (valor * 15 / 100)
print(f'Você temm uma renda de R${valor:.2f} Com o aumento de 15% seu renda vai para R${aumento:.2f}')