print('Olá, tudo bem? preciso que você digite seu nome todo abaixo:')
nome = input('Digite seu nome:')
print(f'Olá {nome} segue as características abaixo')


print(nome.strip())
print(f'seu nome tem {len(nome)} letras')
primeiro_nome = nome.split()[0]
print(len(f'Seu primeiro nome tem {primeiro_nome} letras'))
print(f'Seu nome maiúsculo {nome.upper()}')
print(f'Seu nome minusculo {nome.lower()} ')





 