print('\033[7;0;31mAnálise de dados em uma Tupla\033[m')
print('-=' * 15)
numero = (int(input('Digite um Numero: ')), int(input('Digite o 2° Numero: ')), int(input('Digite 3° Numero: ')), int(input('Digite 4° e Ultimo Numero: ')))
print(f'Vc Digitou os Numeros {numero}')
#count(9)estou contando quantas vezes apareceu o numero 9 
print(f'O Numero 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O Numero 3 apareceu na {numero.index(3)}° posição')
else:
    print('O Numero 3 não foi Digitado em Nenhuma Posição.')
print(f'Os Numeros Pares Digitados São', end=' ')
for num in numero:
    if num % 2 == 0:
        print(num, end=' ')