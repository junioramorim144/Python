nu = int(input('Digite um valor'))
tot = 0
for c in range(1,nu+1):
    if nu % c == 0:
        print('\033[33m',end=' ')
        print(f'{c}',end=' ')
        tot = tot + 1 
    else:
        print('\033[31m',end=' ')
        print(f'{c}',end=' ')
print(f'\n\033[mO número {nu} é dividido {tot} vezes')
if tot == 2:
    print(f'O {nu} é primo!')
else:
    print(f'O número {nu} não é primo!')
    

#fiz sozinho
    