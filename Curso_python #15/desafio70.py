print('$--'* 30)
print('Lojas Super Baratão')
print('$--'* 30)
total = produto1000 = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        produto1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programa!'))
print(f'A Soma total dos produtos comprados foi R${total:10.2f}')
print(f'Temos {produto1000} Custando Mais de Mil Reais')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
     
    



