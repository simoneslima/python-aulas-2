print('-' *40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' *40)
listagem =('Lapis De Cor', 12.50, 'Canetinha', 32.50, 'Caderno', 10.30, 'Borracha', 2.50, 'Lapizeira', 5.90, 'Regua', 3.70, 'Estojo', 13.50)
for iten in range(0, len(listagem)):
    if iten % 2 == 0:
        print(f'{listagem[iten]:.<30}', end='')
    else:
        print(f'R${listagem[iten]:>7.2f}')
print('-' *40)

