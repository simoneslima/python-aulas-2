peso = float(input('Qual é o seu peso? (KG)'))
altura = float(input('Qual é o sua altura? (M)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[7;31mCuidado! Vc esta abaixo do seu peso!\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[7;32mParabéns! Continue assim vc esta na medida certa!\033[m')
elif imc > 25 and imc < 30:
    print('\033[7;33mVc esta em Sobrepeso, ATENÇÂO!\033[m')
elif imc > 30 and imc < 40:
    print('\033[7;33mVc está em Obsidade, ATENÇÂO!!\033[m')
else :
    print('\033[7;31mVoce esta em Obesidade Mórbida, CUIDADO!!!\033[m')
    
