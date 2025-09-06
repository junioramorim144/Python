
opcoes = 0
res = 0
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor: '))
while opcoes != 5:
    

    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números 
    [5] sair do programa''')

    opcoes = int(input('>>>Digite uma opção.'))
    if opcoes == 1:
        res = n1 + n2
        print(f'A soma de {n1} + {n2} é {res} ')
    elif opcoes == 2:
        res = n1 * n2
        print(f'A multiplicão de {n1} x {n2} é {res}')  
    elif opcoes == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}') 
    elif opcoes == 4:
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor: '))
    elif opcoes == 5:
        print('finalizando...')

print('O programa foi fechado.')
