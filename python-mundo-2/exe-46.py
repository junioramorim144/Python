frase = str(input('Digite a frase.')).strip().upper()
frasee = frase.split()
palavra = ''.join(frasee)
inverso = ''
#funciona tambem 
#inverso = palavra[::-1]
for c in range(len(palavra) -1,-1,-1):
    inverso = inverso + palavra[c]
print(inverso)
if palavra == inverso:
    print('Isso é um palíndromo')
else:
    print('Essa palavra não é palíndroma')
