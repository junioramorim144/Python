# co = float (input(' Qual o comprimento do cateto oposto?'))
# ca = float (input(' Qual o comprimento do catelo adjacente?'))

# hi = (co **2 + ca **2) ** (1/2)

# print(f'A Hipotenusa é {hi:.2f}')

from math import hypot
co = float (input ('Qual é o cateto oposto?'))
ca = float (input ('Qual é o cateto adjacente? '))
hi = hypot(co,ca)

print(f'A Hipotenusa é {hi:.2f}')