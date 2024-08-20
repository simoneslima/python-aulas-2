numero = int(input('Digite um numero para fazer a tabuada: '))
for num in range(0,11):
    resultado = numero * num
    print('{} X {} = {}'.format(numero,num, resultado))
