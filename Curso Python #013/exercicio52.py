from sympy import isprime 

# Solicita ao usuário um número para verificar se é primo
numero = int(input("Digite um número: "))

if isprime(numero):
    print('{} É um número primo.'.format(numero))
else:
    print('Não é um número primo.'.format(numero))

