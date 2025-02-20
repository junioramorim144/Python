#Velocidade de uma via
print('Velocidade permitida é 80km.')
fast = int(input('Digite Qual a sua velocidade?'))
pagar = (fast - 80) * 7

if(fast > 80):
    print('VOCÊ FOI MULTADO!')
    print(f'Você passou a {fast} em uma via de 80km.')
    print(f'Você foi multado em {pagar}R$.')
    print('Tenha mais responsabilidade!')
else: print('Você está na velocidade permitida.')
print('Boa viagem!')