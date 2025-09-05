sexo = str (input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo'))
print(f'Seu sexo escolhido é {sexo}.')
