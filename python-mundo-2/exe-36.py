# Formas de pagamento
print('A maquina de lavar roupa custa R$ 4.500 reais.'
      ' Qual será a forma de pagamento?')
valor = 4500
print('(1- A vista)\n' 
                    '(2- cartão)\n' 
                    '(3- 2x cartão)\n' 
                    '(4- 3x cartão)\n')
formas = int (input('Qual a opção?'))
if formas == 1:
    desconto = (valor * 10)/100
    valor_desc = valor - desconto
    print(f'O valor a vista tem 10% de desconto você pagará R$ {valor_desc:.2f} reais.')
elif formas == 2:
    desconto = (valor * 5)/100
    valor_desc = valor - desconto
    print('A vista no cartão tem 5% de desconto você pagará R$'
    f'{valor_desc:.2f} reais') 
elif formas == 3:
    valor_desc = valor / 2
    print('Você pode parcelar em até 2x')
    print(f'Você pagará em duas vezes de R$ {valor_desc:.2f} reais')
elif formas == 4:
     desconto = (valor *20)/100
     valor_desc = valor + desconto
     print('Você pode parcelar em até 3x')
     print('Você pagará 20% de juros em até 3x no cartão.')
     print(f'R${valor_desc:.2f} reais')

