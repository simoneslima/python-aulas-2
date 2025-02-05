estado = dict()
brasil = list()
for c in range(0,3):
    estado['Uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla de Estado: '))
    brasil.append(estado.copy())
#print(brasil) ou fazer mais bonitinho.
for est in brasil:
    for v in est.values():
        print(v, end=' ')
        print()
    '''daria pra fazer dessa forma.'''
    #for k, v in est.items():
        #print(f'A chave {k} tem o valor {v}.')
   