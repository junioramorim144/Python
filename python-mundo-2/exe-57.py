cont = 0 
soma =0
num = 0
num = int(input('Digite um número. [999 para parar:]'))
print('~'* 30)
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número. [999 para parar:]'))
    print('-'*30)

print('_'*30)
print(f'A soma dos {cont} é = {soma }')
print('fechando programa.')