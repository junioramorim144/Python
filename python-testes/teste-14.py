print('Olá, tudo bem? preciso que você digite seu nome todo abaixo:')
nome = input('Digite seu nome:').strip() 
print(f'Olá {nome}, segue as características abaixo')



print('Seu nome tem {} letras'.format(len(nome)- nome.count(' ')))
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome tem {len(primeiro_nome)} letras')
print(f'Seu nome maiúsculo {nome.upper()}')
print(f'Seu nome minusculo {nome.lower()}')





 