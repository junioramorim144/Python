ma = 0
me = 0
for  p in range(1,6):
    peso = float(input(f'Digite o {p}ª peso.'))
    if p == 1: 
       ma = peso
       me = peso
    else:
        if peso > ma:
            ma = peso
        if peso < me:
            me = peso 
print(f' O maior peso lido foi {ma}kg.')
print(f' O menor peso lidp foi {me}kg')


