from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoa)))
    idade = anoAtual- nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior)) 
print('E tivemos {} pessoas de menores de idade'.format(menor))        