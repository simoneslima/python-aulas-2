soma = cont = 0
while True:
 numero = int(input('Digite um valor \033[7;0;31m[999 Para Parar]\033[m: '))
 if numero == 999:
     break
 soma += numero
 cont += 1
 
print(f'Vc digitou {cont}, e a soma entre eles são {soma}')