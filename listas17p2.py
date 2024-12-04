'''pode ser feito assim como esta abaixo.'''
#Valores = list() ou 
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
'''append serve para adicionar elementos na lista'''
#valores.append(5)
#valores.append(4)
#valores.append(3)
#for valor in valores: ou
'''Abaixo vai mostrar a posição e o valor que esta colocado nela.'''
for contador, valor in enumerate(valores):
    print(f'Na posição {contador} encontrei o valor {valor}')
print('Final da lista.')

