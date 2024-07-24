casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salario mensal? R$'))
anos = int(input('Em quantos anos vc quer pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
# A virgula representa o milhar
print('Para pagar uma casa de R${:,.2f} em {} anos '.format(casa, anos), end='') 
print(' a prestação fica em R${:,.2f}'.format(prestacao))
if prestacao <= minimo:
    print('\033[7;32mEmprestimo Concedido!\033[m ')
else:
    print('\033[7;31mEmprestimo Negado!\033[m')