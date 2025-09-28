import random
cont = 1
print(f"{'Jogo do Impar/par':^50}")
while True:
    n = str(input('Impar ou par?')).upper().strip() [0]
    IP = int(input('Digite um number'))
    if cont == 2:
        break
    
    contador = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
    num = random.choice(contador)
    soma =  IP + num
    if soma % 2 == 0:
        print('Par')
    else:
        print('Impar')
    cont += 1    

print(f'Você escolheu {n} e digitou {IP}')
print('*'*10,'Você perdeu!!','*'*10)