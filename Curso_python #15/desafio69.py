print('=-'* 40)
print('Cadastre uma Pessoa')
print('=-'* 40)
tot18 = toth18 = totm20 = 0
while True:
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'MF':
         sexo = str(input('Qual é o Sexo? [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth18 += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
        
        
         
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth18} Homens cadastrado.')
print(f'Ao todo temos {totm20} Mulheres cadastradas com menos de vinte anos.')
     
         
  
    