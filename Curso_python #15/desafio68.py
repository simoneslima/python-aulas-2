# Importa a função randint da biblioteca random para gerar números aleatórios
from random import randint

print('=-'*30)
print('Vamos Jogar Par ou Impar? ')
print('=-'*30)

# Inicializa a variável de contagem de vitórias do jogador
vitoria = 0

# Inicia um loop infinito, que continuará até o jogador perder
while True:
    jogador = int(input('Digite um valor: '))
    
    # Gera um número aleatório entre 0 e 10 para o computador
    computador = randint(0, 10)
    
    # Calcula a soma do valor do jogador com o valor do computador
    total = jogador + computador
    
    # Inicializa a variável tipo com um espaço vazio
    tipo = ' '
    
    # Loop para garantir que o jogador escolha entre "P" (Par) ou "I" (Ímpar)
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    
    # Exibe os valores jogados e o total calculado
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total: {total}', end=' ')
    
    # Verifica se o total é par ou ímpar e imprime o resultado
    print('Deu Par' if total % 2 == 0 else 'Deu Ímpar')
    
    # Verifica a escolha do jogador e compara com o resultado
    if tipo == 'P':
        # Se o jogador escolheu "Par" e o total é par
        if total % 2 == 0:
            print('Você Venceu!!!')
            vitoria += 1  # Incrementa o número de vitórias
        else:
            print('Você Perdeu!!!')
            break  # Sai do loop, encerrando o jogo
    elif tipo == 'I':
        # Se o jogador escolheu "Ímpar" e o total é ímpar
        if total % 2 == 1:
            print('Você Venceu!!!')
            vitoria += 1  # Incrementa o número de vitórias
        else:
            print('Você Perdeu!!!')
            break  # Sai do loop, encerrando o jogo
    
    # Mensagem que indica que o jogo continua
    print('Vamos Jogar Novamente?')
    
# Quando o jogo termina, exibe o número total de vitórias
print(f'GAME OVER! Você venceu {vitoria} vezes.')
 
    
        



    
    
    

    
    