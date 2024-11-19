from random import randint
numeros = (randint(1, 10), randint(1, 10),randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sortiados foram {numeros}')
for num in numeros:
    print(f'{num}', end='  ')
#\n pula para linha de baixo.
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')