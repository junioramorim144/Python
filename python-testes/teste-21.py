import random
print('Tente adivinhar o número:')
sorte = int (input('Digite um número da sorte de 1 a 5:'))
if(sorte > 5): 
    print('Erro! Você digitou um número maior que 5!')
    exit()
    
random_sorte = random.randint(1, 5)
print(random_sorte)

if (sorte == random_sorte):
    print('Parabéns! você acertou em cheio')

else: print('Pouxaa não foi desta vez!!')

    
#Desafio número 28