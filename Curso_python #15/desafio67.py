while True:
    numero = int(input('Quer ver a tabuada de qual numero? '))
    if numero < 0:
        break
    print('-'* 30)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')
    
    print('-'* 30)
print('-'* 30)
print('\033[7;0;31mProcesso finalizado!\033[m')

    
  