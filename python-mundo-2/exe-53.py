'''c = 1 
num = int(input('Digite um valor'))
c = num
f = 1 
print(f'Calculando {num}! =', end=' ')
while c > 0: 
    print( c, end ='  ' )
    print(' x ' if c > 1 else '=', end = ' ')
    f *= c
    c -= 1
print(f)
'''
f = 1 
num = int(input("Digite um número"))
c = num
for c in range( c,0,-1): 
    print(f'{c}',end = ' ')
    print('x' if c > 1 else '=', end =' ')
    f *= c
print(f)
     
    
