temp = []
princ = []
mais = menos = 0
while True:
    temp.append(str(input('NOME: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mais = menos = temp[1]
    else:
        if temp [1] > mais:
            mais = temp[1]
        if temp [1] < menos:
            menos = temp[1]
    princ.append(temp[:])
    temp.clear()            
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo vc cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mais}Kg. Peso de', end='')
for p in princ:
    if p [1] == mais:
        print(f'[{p[0]}]', end='')
print()
print(f'O menos peso foi de {menos}Kg. Peso de ', end='')
for p in princ:
    if p [1] == menos:
        print(f'[{p[0]}]', end='')
print()
