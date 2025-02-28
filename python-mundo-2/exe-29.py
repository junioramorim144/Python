#Covertendo números.
print(f'{'=-'*6} Conversão de números {'=-'*6}')
print(f'{'=-'*6} 1- para binário 2- para octal 3- para hexadecimal {'=-'*6}')
valor = int (input('Digite um número de 1 a 3'))

if valor != 1 and valor != 2 and valor != 3:
    print('ERRO! digite um número de 1 a 3:')

else:
    num = int( input('Digite um valor para conversão:'))

    if (valor == 1):
        print(f'Binário: {bin(num)[2:]}')

    elif (valor == 2):
        print(f'Octal: {oct(num)[2:]}')

    elif (valor == 3):
        print(f'Hexadecimal {hex(num)[2:]}')


