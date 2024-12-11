numeros = list()
while True:
    num = int(input('Digite um valor:'))
    if num not in numeros:
        numeros.append(num)
        print('Adicionado com Sucesso!') 
    else:
        print('Valor duplicado! Não será adicionado!')
        
    continuar = str(input("Quer continuar? (S/N): ")).upper()
    if continuar == 'N':
        break
print('*=*'*30)
numeros.sort()
print(f'Os Numeros Digitados Foram: {numeros}')
    
    