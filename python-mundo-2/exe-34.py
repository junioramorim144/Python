# Triângulo 2.0
r1 = float (input('Digite um valor'))
r2 = float (input('Digite um segundo valor'))
r3 = float (input('Digite um terceiro valor'))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('Os valores podem formar um Triângulo',end='') 
    if r1 == r2 == r3:
        print(' EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO.')
    else:
        print(' ISÓSCELES.')        
else:
    print('Os valores não podem formar um triângulo!')