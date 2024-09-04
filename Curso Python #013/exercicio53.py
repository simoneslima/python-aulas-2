# Exercício Python #053 - Detector de Palíndromo
frase = str(input('Digite uma frase:')).strip().upper()
#fatiamento de palavras
palavras = frase.split()
#juntar a frase
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A Frase digitada não é um Palíndromo!')
 