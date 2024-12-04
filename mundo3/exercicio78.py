numeros = []
for num in range(0, 5):
    numeros.append(int(input('Digite um Valor: ')))

maximo = max(numeros)    
minimo = min(numeros)
print(f'Voce digitou os numeros {numeros}.')

posicoes_max = [i+1 for i, x in enumerate(numeros) if x == maximo]
posicoes_min = [i+1 for i, x in enumerate(numeros) if x == minimo]
print(f'O maior valor foi o numero {maximo} que ficou na posições {posicoes_max}.')
print(f'O menor valor foi o numero {minimo} que ficou na posições {posicoes_min}.')

