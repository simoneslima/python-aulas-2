'''# Exibe o título do programa
print('Sequência de Fibonacci')
# Exibe uma linha de separação
print('-' * 30)

# Solicita ao usuário a quantidade de termos da sequência que ele deseja mostrar
numero = int(input('Quantos termos você quer mostrar? '))

# Define os dois primeiros termos da sequência
termo1 = 0
termo2 = 1

# Exibe outra linha de separação
print('~' * 30)

# Exibe os dois primeiros termos da sequência
print('{} -> {}'.format(termo1, termo2), end='')

# Define o contador para controlar o loop
contador = 3

# Loop para calcular e exibir os próximos termos até alcançar o número desejado
while contador <= numero:
    # Calcula o próximo termo
    termo3 = termo1 + termo2
    # Exibe o próximo termo
    print('-> {}'.format(termo3), end='')
    # Atualiza os valores dos termos
    termo1 = termo2
    termo2 = termo3
    # Incrementa o contador
    contador += 1

# Exibe a mensagem de término
print('-> FIM!')'''

# Codigo simples
numero = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(t1, t2, end=' ')
cont = 3
while cont <= numero:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    cont += 1


    
    
