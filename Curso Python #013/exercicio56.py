soma_idade = 0
media_idade = 0
maior_idade_homem = 0
homem_velho = ''
mulheres_abaixo20 = 0
for pessoa in range(1,5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_abaixo20 += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos '.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, homem_velho))
print('Ao todo são {} mulheres abaixo de 20 anos'.format(mulheres_abaixo20))
            