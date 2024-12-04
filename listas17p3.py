a = [2, 3, 6, 9]
#b = a
b = a[:]
'''Se eu quizer fazer uma copia e mudar uma só lista seria é só colocar [:] aqui estou pedindo para que b receba todos os itens de a ai sim vou fazer uma copia, e poderei mudar só a lista b no caso.'''

b[3] = 7
'''Se eu trocar algum numero como por exemplo 9 por 7, como no exemplo acima irá mudar as duas listas porque elas estão interligadas.'''
'''O nove passará mais não existir em ambas as listas '''
'''Não é uma copia elas estão ligadas!'''

print(f'Lista A: {a}')
print(f'Lista A: {b}')
