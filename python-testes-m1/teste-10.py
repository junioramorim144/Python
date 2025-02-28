dias = int (input('Quantos dias de uso?'))
km = float (input('Quantos km rodados?'))
res = (60 * dias) + (0.15 * km)

print (f'Você usou o carro por {dias} dias e andou {km:.0f} km total a pagar é {res:.2f} R$')