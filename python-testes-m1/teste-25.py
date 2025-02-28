#desafio 33
print('qual é o número menor:')
a = int (input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite p terceiro valor:'))
#menor valor feito na raça 
menor = c
if a < c and a < b:
    menor = a 

if b < a and b < c:
    menor = b

#função feita para descobrir menor/maior valor 
maior = max(a, b, c) #encontra o maior valor das variaveis 
# min() encontra o menor valor   

print(f'O menor número é {menor}')
print(f'O maior valor é {maior}')




