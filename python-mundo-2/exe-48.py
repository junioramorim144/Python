maior = 0
menor = 0

for p in range(1,6):
    peso = float(input(f'Digite o {p}ª peso')) 
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso