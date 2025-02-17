# mostra unidade, dezena , centena, milhar


num = int (input ('Digite um número: '))
if (num > 2000):
    print('Erro!! valor acima do permitido!')
    exit()


n = str(num)
print(f'Analisando o número {n}')

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'A Unidade é {u}')
print(f'A dezena é {d}')
print(f'A centena é {c}')
print(f'O milhar é {m}')



