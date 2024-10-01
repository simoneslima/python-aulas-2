#primeira forma de fazer usando a biblioteca do python.
'''from math import factorial
numero = int(input('Digite um numero para calcular seu fatorial:'))
f = factorial(numero)
print('O fatorial de {} é {}'.format(numero, f))'''

#usando while
'''numero = int(input('Digite um numero para calcular seu fatorial:'))
contador = numero
fatorial = 1
print('\033[7;0;31mCalculando {}=\033[m '.format(numero), end=' ')
while contador > 0:
    print('{}'.format(contador), end='')
    print('x' if contador > 1 else '=', end=' ')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))'''

#usando o for
numero = int(input('Digite um numero para calcular seu fatorial:'))
fatorial = 1
print('\033[7;0;31mCalculando {}=\033[m '.format(numero), end=' ')
for contador in range(numero, 0, -1):
    print('{}'.format(contador), end='')
    print('x' if contador > 1 else '=', end='')
    fatorial *= contador
    
print('{}'.format(fatorial))




