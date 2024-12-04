print('Curso Python #17 - Listas (Parte 1)')
numero = [1, 7, 9, 6]
'''listas são multaveis'''
numero[2] = 3
'''append adiciona'''
numero.append(9)
'''colocara em ordem crescente'''
#numero.sort()
'''colocará em ordem decrescente'''
numero.sort(reverse=True)
'''para inserir o valor na casa que eu quero na casa e o valor'''
numero.insert(0, 8)
'''para remover um valor, quando for colocado .pop sem parametro ele sempre excluirá o ultimo elemento.'''
#numero.pop()
'''se eu colocar o pop(2) vai excluir o numero 2 da lista que no caso é o numero 9.'''
numero.pop(0)
if 6 in numero:
    numero.remove(6)
else:
    print('Não achei 6 da lista!')
print(numero)
'''esse comando conta quantos elementos tem na minha lista'''
print(f'Essa lista tem {len(numero)} elementos.')