mediaidade = 0 
somaidade = 0
quantmulheres = 0
homemvelho = 0 
maisvelho = 0    
for c in range( 1,5):
    print(f'{'-'*5}{c}ª Pessoa{'-'*5}')
    nome = str(input('Digite o nome.')).strip()
    idade = int(input('Digite a idade.'))
    sexo = str(input('Digite o sexo [M/F]')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maisidade = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maisidade:
        maisidade = idade
        homemvelho = nome 
    if sexo in 'fF' and idade < 20:
        quantmulheres + 1 
mediaidade = somaidade/4
#print(mediaidade)

print(f'A média de idade é {mediaidade}')
print(f'O nome do homem mais velho é {homemvelho} com {maisidade} de idade.')
print('A quantidade de mulher com menos de 20 é {quantmulheres}')         
    



    

