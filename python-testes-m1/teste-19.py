nome = str (input('Digite seu nome por favor:'))
nome_dividido = nome.split()

primeiro_nome = nome_dividido[0]
ultimo_nome = nome_dividido[-1]

print(f'Prazer em te conhecer {nome}!')
print(f'Seu primeiro nome é {primeiro_nome}.')
print(f'Seu ultimo nome é {ultimo_nome}.')