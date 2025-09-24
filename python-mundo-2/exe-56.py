print('Sequencia de Fibonacii')
print('-'*30)
nu = int(input('Digite o primeiro número:'))
t1 = 0
t2 = 1
c = 1
print('~'*30)
while c <= nu:
    print(f'{t1} {t2}', end='')
    t3 = t1 + t2
    print(t3,end='')
    c += 1 