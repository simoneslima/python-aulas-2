#Tuplas são imutaveis, isso quer dizer que não vou conseguir atribuir novos valores a esta tupla.
from time import sleep
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudin', 'Batata Frita')
#len busca quantas comidas tem na tupla 
print('Temos', end=' ')
print(len(lanche), end=' ')
print('Lanches.')
#Sorted é um comando para organizar as posições por ordem alfabetica.
print(sorted(lanche))
print('O que vai pedir? ')
sleep(3)
# exemplos de for que tem o mesmo resultado
# 1 Exemplo:
'''for comida in lanche:
    print(f'Eu vou pedir {comida}')'''
    
# 2 Exemplo:
'''for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')'''
    
# Exemplos:(para mostrar posições se for preciso mostrar posições.)  
# 1 Exemplo: 
'''for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''
    
# aqui tem duas variaveis separado por virgula    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
sleep(3)    
print('Comi pra Caramba!...')

