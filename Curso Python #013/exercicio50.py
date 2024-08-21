n1 = int(input('Digite O Primeiro numero para soma:'))
n2 = int(input('Digite O Segundo numero para soma:'))
n3 = int(input('Digite O Terceiro numero para soma:'))
n4 = int(input('Digite O Quarto numero para soma:'))
n5 = int(input('Digite O Quinto numero para soma:'))
n6 = int(input('Digite O Sexto e ultimo numero para soma:'))

# Coloca os números em uma lista
lista = [n1, n2, n3, n4, n5, n6]

soma = 0

for numero in lista:
    if numero % 2 == 0:
        soma += numero  # Soma apenas os números pares

print('A soma dos números pares é: {}'.format(soma))
