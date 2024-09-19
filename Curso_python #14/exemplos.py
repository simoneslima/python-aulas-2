print('Curso Python #014 - Estrutura de repetição while')
#Uma das maneiras de fazer nesse caso eu usaria o for porque sei o limite.
'''for c in range(1, 10):
    print(c)
print('Fim') '''

 # usando o WHILE que é mais usado para quando não sabemos o limite.
'''c = 1
while c < 10:
     print(c)
     c = c + 1 
print('Fim')'''     

# outro exemplo
'''for c in range(1,5):
    valor = int(input('Digite um valor: '))
print('Fim')'''

# enquanto o valor for diferente de 0 continuar perguntando.
# não daria pra fazer isso com o for porque não tem limite o ponto de parada seria o 0.
'''valor = 1
while valor != 0:
    valor = int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')'''

# usando o FOR
'''for c in range(1,5):
    numero = int(input('Digite um valor: '))
print('FIM')'''

# ou poderia fazer o mesmo com while acima eu estabeleci um limite. 
# aqui sera enquanto a pessoa nao digita o numero 0 não finaliza.
'''numero = 1
while numero != 0:
    numero = int(input('Digite um valor: '))
print('Fim!')'''

# outro exemplo:
'''resposta = 'SIM'
while resposta == 'SIM':
    numero = int(input('Digite um valor:  '))
    resposta = str(input('Quer continuar [SIM/NÃO] ')).upper()
print('Fim!')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} numeros impares.'.format(par, impar))





    