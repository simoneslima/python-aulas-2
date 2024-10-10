resp = 'S'  # Inicializa a variável de resposta com 'S' (Sim)
soma = quant = media = maior = menor = 0  # Inicializa as variáveis para soma, quantidade, média, maior e menor

while resp in 'Ss':  # Continua o loop enquanto a resposta for 'S' ou 's'
    numero = int(input('Digite um numero:'))  # Pede ao usuário um número
    soma = soma + numero  # Adiciona o número à soma
    quant = quant + 1  # Incrementa a quantidade de números digitados

    if quant == 1:  # Se for o primeiro número, define o maior e o menor como o próprio número
        maior = menor = numero
    else:
        if numero > maior:  # Atualiza o maior número, se o número atual for maior
            maior = numero
        if numero < menor:  # Atualiza o menor número, se o número atual for menor
            menor = numero

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]  # Pergunta ao usuário se quer continuar

media = soma / quant  # Calcula a média dos números digitados
print('Vc digitou {} números, a soma de todos os numeros foi {} e a média dos números somados foi {}'.format(quant, soma, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))  # Exibe o maior e menor número


