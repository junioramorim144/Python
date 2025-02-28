# Programa natação
print('Bem vindo a confederação nacional de natação.')
print('Abaixo, Digite o ano de nascimento.')
ano_idade = int (input('Digite seu ano de nascimento com 4 digitos:'))

idade = 2025 - ano_idade
#print(idade)
if idade <= 9:
    print('Você se enquadra na categoria mirim')
elif idade > 9 and idade <= 14: 
    print('Você se enquadra na categoria infantil')

