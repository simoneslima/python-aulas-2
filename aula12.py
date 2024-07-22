nome = input('Qual é o seu Nome? ').strip()
banda = input('Qual banda você mais gosta? ').strip().upper()

if banda == 'QUEEN':
    print('Queen é uma banda incrível!!!')
elif banda == 'LED ZEPPELIN' or banda == 'THE CARPENTERS' or banda == 'RUSH' or banda == 'SHOCKING BLUE':
    print('Parabéns, pelo bom gosto!')
elif banda in 'GOLDEN EARRING THE HOLLIES THE ZOMBIES THE KINKS CREEDENCE CLEARWATER REVIVAL FREDDIE AND THE DREAMERS':
    print('Você é incrível!')
else:
    print('Ainda assim, é muito legal!')

print('Tenha um ótimo dia, {}!'.format(nome))


