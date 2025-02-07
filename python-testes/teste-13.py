import random
n1 = str (input('Qual é o primeiro nome:'))
n2 = str (input('Qual é o Segundo  nome:'))
n3 = str (input('Qual é o terceiro nome:'))
n4 = str (input('Qual é o quarto nome:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print (f'O aluno escolhido foi {escolhido}')

#ou


#from random import choice
#n1 = str (input('Qual é o primeiro nome:'))
#n2 = str (input('Qual é o Segundo  nome:'))
#n3 = str (input('Qual é o terceiro nome:'))
#n4 = str (input('Qual é o quarto nome:'))
#lista = [n1, n2, n3, n4]
#escolhido = choice(lista)
#print (f'O aluno escolhido foi {escolhido}')
