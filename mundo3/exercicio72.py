num_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
               'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
               'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
               'Dezenove', 'Vinte')

while True:
    # Solicita o número e verifica se está no intervalo permitido
    while True:
        num = int(input('Digite um Número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    
    # Exibe o número por extenso
    print(f'Você digitou o número {num_extenso[num]}')
    
    # Pergunta se o usuário quer continuar
    continua = ' '
    while continua not in 'SN':
        continua = input('Você quer continuar? [S/N] ').strip().upper()[0]
    
    # Sai do loop se o usuário não quiser continuar
    if continua == 'N':
        print("Programa finalizado.")
        break

    

            
          
        
         


        
 
