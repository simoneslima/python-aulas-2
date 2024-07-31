nota1 = float(input('Sua primeira nota: '))
nota2 = float(input('Sua seguna nota: '))
resultado = (nota1 + nota2) / 2
print('Sua Média é {}'.format(resultado))
if resultado > 7:
    print('Vc foi \033[6;32mAPROVADO\033[m, Parabéns!')
elif resultado < 7 and resultado > 5:
    print('Vc esta em \033[6;33mRECUPERAÇÃO!\033[m Boa Sorte na proxima tentativa!')
else:
    print('Vc foi \033[6;31mREPROVADO!\033[m')
    

