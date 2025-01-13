bandas = list()
dados = list()
totmaior = totmenor = 0
for c in range(0, 5):
    dados.append(str(input('Banda: ')))
    dados.append(int(input('Quat Integrantes')))
    bandas.append(dados[:])
    dados.clear()
print(bandas)

for integ in bandas:
    if integ[1] >= 3:
        print(f'{integ[0]} tem mais integrantes ')
        totmaior += 1
    else:
        print(f'{integ[0]} tem menos integrantes')
        totmenor += 1
print(f'Temos {totmaior} bandas com mais de 3 integrantes e {totmenor} com menos de 3 integrantes.')