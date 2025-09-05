import random
chute = 0 
random_pc = random.randint(1,10)
print(f'{'_'*5}Adivinhe o número.{'_'*5}')
n = int(input('chute um número'))
while random_pc != n:
    n = int(input('Você errou! tente novamente'))
    chute += 1 
print(f' Você acertou mas a quantidade de chutes foram {chute} vezes!')

