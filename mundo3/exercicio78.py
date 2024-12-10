numeros = []
maximo = 0  
minimo = 0
for num in range(0, 5):
    numeros.append(int(input(f'Digite um Valor na posição {num}: ')))
    if num == 0:
        maximo = minimo = numeros[num]
    else:
        if numeros[num] > maximo:
            maximo = numeros[num]
        if numeros[num] < minimo:
            minimo = numeros[num]
print('=-='* 30)
print(f'Voce digitou os numeros {numeros}.')
print(f'O maior valor foi o numero {maximo} que ficou nas posições.', end='')
for i, v in enumerate(numeros):
    if v == maximo:
        print(f'{i}, ', end='')
print()
print(f'O menor valor foi o numero {minimo} que ficou nas posições.', end='')
for i, v in enumerate(numeros):
    if v == minimo:
        print(f'{i}, ', end='')
print()

