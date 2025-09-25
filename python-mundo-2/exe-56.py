print('Sequencia de Fibonacci')
print('-'*30)
nu = int(input('Digite o número'))
print('-'*30)
t1 = 0
t2 = 1
c = 3 
print('~'*30)
print(f'{t1} -> {t2}', end=' ')
while c <= nu:
    t3 = t1 + t2
    print(f'-> {t3}',end=' ')
    c += 1 
    t1 = t2
    t2 = t3
print('-> Fim.')    