from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('   Jogar na Mega Sena   ')
print('-' * 30)
quantidade = int(input('Quantos jogos quer Sortear? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-'* 3, f'Sorteando {quantidade} Jogos','-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('**'*5, f'Boa sorte!', '**'*5)


        
