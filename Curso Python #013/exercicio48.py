soma = 0 #acumulador
cont = 0 #contador
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        cont = cont + 1
        soma = soma + contador
print('A soma de todos os {} números no intervalo de 3 é {}'.format(cont,soma))
    
    
        
    
   

    
    

   
