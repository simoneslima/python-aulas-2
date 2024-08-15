#contagem regressiva
for nome in range(7, 0, -1):
  print(nome)
print('Fim')

#pula a cada duas casas
for nome in range(0, 8, 2):
  print(nome)
print('Fim')

#contar até o numero que digitei
numero = int(input('Digite um numero: '))
for num in range(0, numero+1):
    print(num)
print('FIM') 

#do inicio ao fim em quantos passos 
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')

#vai pedir 3 valores
for b in range(0, 3):
    numero = int(input('Digite um valor!'))
print('Fim')

#vai fazer a soma    
s = 0    
for b in range(0, 3):
    numero = int(input('Digite um valor!'))
    #ou poderia simplificar 
    s += numero
    #s = s + numero
print('A soma de todos os numeros foi {}'.format(s))


   