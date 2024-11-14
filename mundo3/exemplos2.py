a = (2, 5, 6)
b = (4, 7, 9, 2)
# vai mostrar na ordem
c = a + b
print(c)
#mostra quantos elementos tenho na tupla
'''print(len(c))'''

#posso fazer uma pequena pesquisa quantas vezes aparece o numero 2 no C
'''print(c.count(2))'''

#em que posição está, coloca o numero para saber, ele sempre pega a primeira ocorrencia, estou me referindo a numero repitido.
'''print(c.index(5))'''

#Aqui vou ignorar a posição 0 e começo da posição 1 ate encontrar nas outras posições o numero que quero no caso o 2.
print(c.index(2 , 1))

#nas tuplas eu posso colocar tanto numero quanto strings
objeto = ('caderno', 5,12, 'Caneta', 2,50, 'Lapís', 1,25)
del(objeto)
print(objeto)

#se eu quizer apagar uma tupla eu digito
'''del(e o nome da tupla que apaga ela inteira!)'''
#mas eu não posso apagar 1 iten na tupla só a tupla inteira
