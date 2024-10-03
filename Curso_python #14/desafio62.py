print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o Termo:'))
razão = int(input('Digite a Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais!= 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa...')
    mais = int(input('Quantos termos vc quer mostrar a mais: '))
print('Progresão finalizada com {} termos mostrados'.format(total))