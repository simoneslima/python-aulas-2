num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print('\033[7;36;41mO numero {} é maior!\033[m '.format(num1))
elif num2 > num1:
    print('\033[7;36;41mO numero {} é maior!\033[m '.format(num2))
else:
    print('\033[7;33;32mOs dois numeros são iguais!\033[m')