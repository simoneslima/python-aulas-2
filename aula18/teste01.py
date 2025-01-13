teste = list()
teste.append('Simone')
teste.append(41)
galera = list()
# Abaixo foi criado uma copia 
galera.append(teste[:])
teste[0] = 'Freddie Mercury'
teste[1] = 42
# Aqui tb foi criado uma copia que ira pegar os dois nomes e idades.
galera.append(teste[:])
print(galera)