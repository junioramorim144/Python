primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))

n1 = primeiro
c = 1
total = 0
mais = 10
while mais != 0: 
    total += mais 
    while c <= total:
        print( n1)
        n1 += razao 
        c += 1 
    mais = int(input('Deseja fazer mais quantos?')
               )
print('Programa fechado.')

