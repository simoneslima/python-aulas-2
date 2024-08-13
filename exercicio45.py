from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('\033[7;0;32mJO\033[m')
sleep(1)
print('\033[7;0;32mKEN\033[m')
sleep(1)
print('\033[7;0;32mPO!!!\033[m')
print('-=' * 12)
print('\033[7;0;33mComputador jogou {}\033[m'.format(itens[computador]))
print('\033[3;0;31m-=\033[m' * 12)
print('\033[7;0;35mJogador jogou {}\033[m'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('\033[7;0;32mEMPATE!\033[m')   
    elif jogador == 1:
        print('\033[7;0;35mJOGADOR VENCE!\033[m')
    elif jogador == 2: 
        print('\033[7;0;33mCOMPUTADOR VENCE!\033[m')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:
    if jogador == 0:
        print('\033[7;0;33mCOMPUTADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[7;0;32mEMPATE\033[m')
    elif jogador == 2:
        print('\033[7;0;35mJOGADOR VENCE!\033[m')
    else:
        print('JOGADA INVALIDA!')
        
elif computador == 2: 
    if jogador == 0:
        print('\033[7;0;35mJOGADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[7;0;33mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[7;0;32mEMPATE!\033[m')
    else:
        print('JOGADA INVALIDA!')
        
        