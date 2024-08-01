from datetime import date
ano_atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - nascimento
print('O atleta tem {}'.format(idade))
if idade < 9:
    print('Classificação Mirin')
elif idade < 14:
    print('Classificação Infantil') 
elif idade < 19:
    print('Classificação Junior') 
elif idade < 25:
    print('Classificação Sênior')
else:
    print('Classificação Master')  