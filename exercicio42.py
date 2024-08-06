angulo1 = float(input('Primeiro Segmento: '))
angulo2 = float(input('Segundo Segmento: '))
angulo3 = float(input('Terceiro Segmento: '))
if angulo1 < angulo2 + angulo3 and angulo2 < angulo1 + angulo3 and angulo3 < angulo1 + angulo2:
    print('\033[7;32mOs segmentos acima pode formar um triangulo\033[m'
,end='')
    if angulo1 == angulo2 == angulo3:
        print('\033[7;32m Equilátero\033[m')
    elif angulo1 != angulo2 != angulo3 != angulo1:
        print('\033[7;32m Escaleno\033[m')
    else:
        print('\033[7;32m Isósceles\033[m')
else:
    print('Os segmentos acima \033[7;31mNÃO PODEM FORMAR TRIANGULO!\033[m')