frase = str(input ('Digite uma frase para nós!')).upper() .strip()
print(f"A letra (A) aparece {frase.count('A')} vez/vezes")
print(f"A letra (A) aparece na primeira posição {frase.find('A') + 1}")
print(f"A letra (A) aparece por ultimo na posição {frase.rfind('A') + 1}")

print('Fiz Sozinho!')
