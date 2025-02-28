#finaciamento de uma casa
print('Olá, bem vindo ao financiamento do seu lar!')
print('Vamos verificar se seu Empréstimo será aprovado:')

emprestimo = float(input('Qual o valor do empréstimo?'))
parcelas = int(input('Quantas parcelas você deseja para o empréstimo?'))
pagamento = float(input('Qual sua renda mensal?'))

emp_parcelas = emprestimo / parcelas
pagamento_parcelas = pagamento * 0.30

print(f'Valor do Empréstimo: R$:{emprestimo:.2f} ')
print(f'Parcelas de: {parcelas} vezes')
print(f'Sua renda é de: R$:{pagamento:.2f} reais')
print('O valor da parcela não pode passar de 30% do seu pagemento!')



if emp_parcelas > pagamento_parcelas:
    print('Ops! sua parcela passa de 30% do seu pagamento')

else:
    print('Seu empréstimo foi aprovado!')


print (f'{emp_parcelas:.2f}')










