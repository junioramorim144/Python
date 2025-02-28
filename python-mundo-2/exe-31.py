# Apresentação ao exército brasileiro 
print('Bem vindo ao site do Exército brasileiro')
print('Digite seu ano de nascimento abaixo:')
ano = int (input('Insira seu ano de nascimento com os 4 digitos:'))

idade = 2025 - ano 
print(f'Você tem {idade}')

if idade == 18:
    print('Você precisa se apresentar no exército brasileiro!')
elif idade < 18:
    print('Você ainda não está na idade de se apresentar ao exército!')
else:
    print('Você passou da idade de se apresentar!')
    print('Caso não tenha se apresentado, Por favor procure uma base militar!')
