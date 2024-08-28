soma = 0
cont = 0
for contador in range(1, 7):
  numero = int(input('Digite o {}° numero para soma:'.format(contador)))
  if numero % 2 == 0:
    soma = soma + numero
    cont = cont + 1
print('Foi informado {} numeros pares e a soma deles são {}'.format(cont, soma))
  
