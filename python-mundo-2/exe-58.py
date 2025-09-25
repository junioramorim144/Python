resp = 'S'
soma = quant = media = menor = maior = 0
while resp in 'sS':
    num = int(input('Digite um número'))
    soma += num 
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
media = soma / quant
print(f'Você Digitou {quant} números e a  media é {media}')  
print(f'O maior número foi {maior} e o menor foi {menor}')
  















# c = 0
# s = 'S'
# opcao = 'S'
# soma = 0
# while opcao == s:
#     num = int(input('Digite um número:'))
#     opcao = str(input('Quer continuar?[S/N]'))
#     soma += num
#     c += 1
# res = num / c
# print (f'Você digitou {c} números e a média foi {res}') 

