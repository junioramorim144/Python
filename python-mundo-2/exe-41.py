print(f'{'-'*10}Tabuada{'-'* 10}')
op = int(input('Qual tabuada você deseja?'))
tipo = str(input('divisao, multiplicação ou subtração?'))
if op == 0 or op > 10:
    print('Erro! Digite uma tabuada de 1 a')
