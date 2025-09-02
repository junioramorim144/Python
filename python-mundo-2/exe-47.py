from datetime import date 
ano = date.today().year
totmaior = 0
totmenor = 0
for r in range(1,8):
    nasc = int(input(f'Digite o ano de nascimento da {r}ª pessoa.')) # alt + 166
    idade = ano - nasc
    if idade >= 18:
        print(f'Você já tem {idade} é de maior')
        totmaior += 1
    else:
        print(f'Você tem {idade} é de menor')
        totmenor += 1
print('-'*40)        
print(f'O total de maiores é {totmaior}')
print(f'O total de menores é {totmenor}')