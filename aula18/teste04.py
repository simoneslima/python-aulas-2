bandas = list()
dados = list()
for c in range(0, 5):
    dados.append(str(input('Banda: ')))
    dados.append(int(input('Quat Integrantes')))
    bandas.append(dados[:])
    dados.clear()
print(bandas)