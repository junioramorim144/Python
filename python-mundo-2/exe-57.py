cont = 0 
soma =0
nu = 0
num = int(input('Digite um número. [999 para parar:]'))
while num != 999:
    soma += num
    cont += 1 
print(f'A soma dos {cont} é = {soma }')
print('fechando programa.')