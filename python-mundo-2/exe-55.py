termo1 = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))

t = termo1
r = razao
c = 1 

while(termo1 <= 10):
    print(f'{t} ->', end ='')
    t += r
    c += 1