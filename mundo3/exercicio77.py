bandas = ('Queen', 'Carpenters', 'Led Zeppelin', 'Rush', 'Shocking Blue', 'Zombies', 'Holies', 'Golden Earring','Creedence Clearwater Revival', 'Jackons 5')
for banda in bandas:
    print(f'\nNa palavra {banda.upper()} temos as vogais: ',end=' ')
    for vogal in banda:
        if vogal.lower() in 'aeiou':
            print(vogal, end='')
