#Qual número é maior
n1 = int(input('Digite o primeiro número'))
n2 = int (input('Digite o segundo número'))
 
print('Agora vamos comparar e saber quem é o maior!')

if n1 > n2:
    print(f'O número {n1} é maior')
elif n2 > n1:
    print(f'O número {n2} é maior')
else:
    print(f'Os números são iguais!')    