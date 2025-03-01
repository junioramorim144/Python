# média dos alunos. 

nota1 = float (input('Digite sua primeira nota:'))
nota2 = float (input('Digite sua segunda nota:'))
nota = [nota1, nota2]
media = sum(nota) / len(nota)
#print(media)

if media < 5.0:
    print(f'Você reprovou tirou {media}')
elif media >= 5.0 and media <= 6.9:
    print(f'Você está em recuperação {media}')
else: 
    print(f'Você está aprovado {media}')