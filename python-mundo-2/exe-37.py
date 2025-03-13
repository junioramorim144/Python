# Jogo Jokenpô
import random
print(("-="*4)+'Vamos jogar Jokenpô?'+("-="*4))
print('escolha um desses...\n'
      '1 = Pedra\n' 
      '2 = Pepel\n'
      '3 = Tesoura\n')
num = int(input('Qual foi a escolha?'))
print('vamos ver se consegue ganhar da máquina!')
jokenpo = [1, 2 , 3]
num2 = random.choice(jokenpo)
print(num2)
if num == num2:
    print('Empatamos')
elif num == 1 and num2 == 2:
        print('Você jogou pedra\n Eu joguei papel\n eu ganhei!')  
elif num == 1 and num2 == 3:
        print('Você jogou pedra\n Eu joguei tesoura\n eu perdi!')
elif num == 2 and num2 == 1:
        print('Você jogou papel\n eu joguei pedra\n eu perdi!')
        
        
        #voltarei para consertar este código!