# Calculo do IMC 
print(("-"*4) +' Calculando o imc '+("-"*4))
peso = float(input('Digite seu peso (kg)'))
altura = float(input('Digite sua altura (m)'))
imc = peso / (altura**2)
print(f'Você pesa {peso} kg e tem {altura} de altura.')
print(f'Seu imc é {imc:.2f}')
if(imc < 18.5):
    print('Abaixo do peso')
elif( 18.5 <= imc < 25):
    print('Peso normal')
elif(25 <= imc < 30):
    print('Sobrepeso')
elif(30 <= imc < 35):
    print('Obesidade Grau 1')
elif(35 <= imc < 40):
    print('Obesidade de Grau 2 (severa)')
else:
    print('Obesidade Grau 3 (mórbida)')

