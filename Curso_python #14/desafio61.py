print('Gerador de PA')
print('-=' * 10)
primeiroTermo = int(input('Digite o Termo:'))
razão = int(input('Razão da PA: '))
termo = primeiroTermo
cont = 1
while cont <= 10:
    print('{}-> '.format(termo), end='')
    termo = termo + razão
    cont += 1
print('FIM!')
