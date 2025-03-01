# Programa natação
from datetime import date
atual = date.today().year
print('Bem vindo a confederação nacional de natação.')
print('Abaixo, Digite o ano de nascimento.')
ano_idade = int (input('Digite seu ano de nascimento com 4 digitos:'))

idade = atual - ano_idade
#print(idade)
if idade <= 9:
    print('Você se enquadra na categoria Mirim')
elif  idade <= 14:  #idade > 9 and 
    print('Você se enquadra na categoria Infantil')
elif idade <= 19:
    print('Você se enquadra na categoria Junior')
elif idade == 25:
    print('Você se enquadra na categoria Sênior')
else:
    print('Você se enquadra na categoria Master')    
