pessoas = {'nome':'Simone', 'sexo':'F', 'idade': 40}
'''Foi deletado o sexo'''
'''posso adicionar tambem.'''
pessoas['peso'] = 72.2
#del pessoas['sexo']
'''Fazer uma mudanção de nome.'''
#pessoas['nome'] = 'Quiteria'
'''vai mostrar tudo que tem lista.'''
#print(pessoas)
'''Vai mostrar o que tem na chave nome'''
#print(pessoas['nome'])
'''se eu quiser formatar tenho que colocar aspas duplas já que comecei com aspas simples.'''
#print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
'''Aqui ira printar só as chaves.'''
#print(pessoas.keys())
'''Ira mostrar os dados(valores).'''
#print(pessoas.values())
'''Abaixo irá mostrar tanto as chaves quanto os valores(os dados).'''
#print(pessoas.items())
#for k in pessoas.values():
for k, v in pessoas.items():
    print(f'{k} = {v}')
    