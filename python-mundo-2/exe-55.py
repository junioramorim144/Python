print('Gerador de PA')
print('-='*10)
n1 = int(input('Digite o primeito valor:'))
razao = int(input('Digite a razao:'))
termo = n1
total = 0
mais = 10
c = 1 
while mais != 0:
    total += mais  
    while c <= total:
        print(f'{termo} ->', end=' ')
        termo += razao
        c += 1
        
    mais = int(input('Quantos termos você quer mostrar?'))
print('fechando programa...')

