print('Olá, Tudo bem?')
print('-----Vamos calcular o valor da sua passagem-----')
km = float (input('Digite os km da sua viagem'))

print ('Vamos cobrar 0,50 centavos por km. e 0,45 centavos por km em viagens superiores a 200km:')

if (km <= 200):
    viagem = km * 0.50 
    print(f'Sua viagem ficou em R${viagem} reais ')
else:
    viagem2 = km * 0.45
    print(f'Sua viagem ficou em R${viagem2} reais ')
