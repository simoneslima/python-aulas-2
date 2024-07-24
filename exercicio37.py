numero = int(input('Digite um numero inteiro: '))
print ('''Escolha uma das bases para conversão: 
       [1] Converter para BINÁRIO
       [2] Converter para OCTAL 
       [3] Converter para HEXADECINAL''')
opção = int(input('Sua Opção: '))
if opção == 1:
    #Esse [2:] significa que eu fatiei e não quero que mostre os dois primeiros caracteres.
    print('{} Convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECINAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('\033[7;31mNumero Invalido! Digite uma das opções acima:\033[m ')