print('{:=^40}'.format('\033[6;0;32m LOJAS SIMONE \033[m'))
preco = float(input('Preço das compras? '))
print('''FORMAS DE PAGAMENTO: 
      [1] Á VISTA dinhiro/cheque
      [2] Á VISTA no cartão
      [3] 2x SEM JUROS no cartão
      [4] 3x ou mais no CARTÃO com juros''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco 
    parcela = preco /  2
    print('Sua parcela ficará em R${:.2f} sem juros .'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas Parcelas? '))
    parcela = total / totparc
    print('Será parcelada em {} de R${:.2f} com juros.'.format(totparc, parcela))
else:
    total = 0
    print('\033[7;0;31mOPÇÃO INVALIDA! TENTE NOVAMENTE...\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))