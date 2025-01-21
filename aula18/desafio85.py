numero = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input('Digite o {c}° valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print('-=-'*30)
numero[0].sort()
numero[1].sort(5)
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'os valores impares digitados foram: {numero[1]}')

    
