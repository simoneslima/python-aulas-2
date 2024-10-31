print('='* 30)
print('{:^30}'.format('Banco Vem Pra Cá Que Tem!'))
print('='* 30)
# Solicita o valor do saque ao usuário e converte para inteiro
valor = int(input('Qual valor do saque? R$'))

# Define o valor total do saque e inicia as variáveis para controle das cédulas
total = valor           # Variável que armazena o valor restante do saque
ced = 100               # Valor inicial da cédula (começando pela maior)
totalced = 0            # Contador para o número de cédulas de cada valor

# Loop principal para determinar a quantidade de cada cédula no saque
while True:
    # Verifica se o valor restante é maior ou igual ao valor da cédula atual
    if total >= ced:
        total -= ced     # Subtrai o valor da cédula do valor total restante
        totalced += 1    # Incrementa o contador de cédulas do valor atual
    else:
        # Se há cédulas do valor atual, imprime a quantidade
        if totalced > 0:
            print(f'Total de {totalced} notas de R${ced}')
        
        # Altera o valor da cédula para a próxima menor, seguindo a ordem 50 -> 20 -> 10 -> 1
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        
        # Reinicia o contador de cédulas para o próximo valor de cédula
        totalced = 0

        # Se o valor restante total for zero, encerra o loop
        if total == 0:
            break

print('=' * 30)
print('Saque finalizado com Sucesso! Volte Sempre!')

                
        
