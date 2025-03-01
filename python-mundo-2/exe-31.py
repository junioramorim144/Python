# Apresentação ao exército brasileiro 
from datetime import date
atual = date.today().year
print('Bem vindo ao site do Exército brasileiro')
print('Digite seu ano de nascimento abaixo:')
ano = int (input('Insira seu ano de nascimento com os 4 digitos:'))

idade = atual - ano 

print(f'Quem nasceu em {ano} tem {idade} ano em {atual}')

if  idade == 18:
     print('Você precisa se apresentar no exército brasileiro!')

elif idade < 18:
     saldo = 18 - idade
     print(f'Você ainda não tem 18 anos. ainda faltam {saldo} anos para 18 anos!')

else:
     saldo = idade - 18
     ano = atual - saldo
     print(f'Você já deveria ter se alistado há {saldo} anos!')
     print(f'Seu alistamento foi  há {ano} anos')

