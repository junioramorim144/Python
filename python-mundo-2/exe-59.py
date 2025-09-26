 
cont = soma = 0 
while True:
    num = int(input('Digite um número: (666 para parar):'))
    if num == 666:
        break
    soma += num
    cont += 1 
print('-'*30)
print(f'Totais de número digitados {cont}')
print(f'A soma entre eles é = a {soma}!')