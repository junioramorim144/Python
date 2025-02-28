# Desafio 34
# calculo de aumento de salario 
def calcular_porcentagem(valor, porcentagem):
    return (valor * porcentagem) / 100

print('Bem vindo!')
salario = float(input('Digite seu salário:'))

if (salario > 1250.00 ):
    aumento1 = calcular_porcentagem(salario, 10)
    salario_aumento = salario + aumento1
    print(f'Seu aumento é de R$ {aumento1:.2f}' )
    print(f'Seu salário com 10% de aumento R$ {salario_aumento:.2f}')
    

else:
    aumento = calcular_porcentagem(salario, 15)
    salario_aumento = salario + aumento
    print(f'Seu aumento é de R$ {aumento:.2f}' )
    print(f'Seu salário com 15% de aumento R$ {salario_aumento:.2f}')

