print('-'*40)
print('\033[7;0;36mTratando vários valores\033[m')
print('-'*40)
'''Simplificando isso
num = 0
cont = 0
soma = 0'''
num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    cont += 1
    soma = soma + num 
    num = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma)) 
    
