nota1 = float (input('Digite sua primeira nota:'))
nota2 = float (input('Digite sua segunda nota:'))



if (nota1 > 10  or nota2 > 10 ):
    print('Erro!! sua nota náo pode ser maior que 10')
    exit()

else: 
    media = (nota1 + nota2) / 2

if( media >= 6):
    print('Parabéns! sua media vai bem!')

else: print('Você precisa estudar mais, campeão!')

print (f'{media}')
