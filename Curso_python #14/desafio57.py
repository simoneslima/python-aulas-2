'''sexo = str(input('Digite o sexo: ')).upper()

while sexo not in ('M', 'F'):
    print('Sexo inválido! Digite novamente!')
    sexo = str(input('Digite o sexo: ')).upper()  # Aqui é onde você atualiza o valor

print('Sexo {} registrado com sucesso!'.format(sexo))'''

# corrigindo 
sexo = str(input('Imforme seu sexo: [M/F]')).strip().upper()[0] # o zero é para pegar a primeira letra caso digito a palavra inteira.
while sexo not in 'MF':
    sexo = str(input('Dados invalido! Digite novamente: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso! '.format(sexo))    




