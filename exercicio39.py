from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Qual é o seu ano de nascimento? '))
idade = ano_atual - ano_nasc
print('Quem nasceu em {} tem {} anos em {}'.format(ano_nasc, idade, ano_atual))
if idade == 18:
    print ('Já esta na hora de se alistar! ')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para se alistar!'.format(saldo))
    ano = ano_atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Vc já deveria ter se alistado há {}! '.format(saldo))
    ano = ano_atual - saldo
    print('Seu alistamento foi em {}'.format(ano))