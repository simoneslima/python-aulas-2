n1 = int(input('\033[7;0;34mDigite o primeiro numero: \033[m'))
n2 = int(input('\033[7;0;34mDigite o segundo numero: \033[m'))
opcao = 0
while opcao != 5:
    print('''\033[7;0;32m
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Retornar
        [5] Sair\033[m''')
    opcao = int(input('Qual é a sua opcão? '))
    if opcao == 1:
        soma = n1 + n2
        print('\033[7;0;30mA soma de {} mais {} é igual á {}\033[m'.format(n1,n2,soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('\033[7;0;30mMultiplicando {} vezes {} vai dar {}\033[m'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2 
        print('\033[7;0;30mEntre os numeros {} e {} o maior numero é {}\033[m'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('\033[7;0;34mDigite o primeiro numero:\033[m'))
        n2 = int(input('\033[7;0;34mDigite o segundo numero: \033[m'))
    elif opcao == 5:
        print('Finalizando o Programa!')
    else:
        print('\033[7;31mOpção Invalida! Tente Novamente!\033[m')
    print('=-='* 10)
        
print('Fim do Programa!')
