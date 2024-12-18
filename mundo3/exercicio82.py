numero = []
pares = []
impares = []
while True:
    numero.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    
print(f'Os numeros digitados foram: {numero}')
print(f'Os numeros pares são: {pares}')  
print(f'Os numeros impares são: {impares}')  
