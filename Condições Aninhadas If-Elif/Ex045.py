#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
import emoji
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(emoji.emojize('''\033[1;31mPlay time!!!!!!!\033[0;0m\033[1;36m
[0] PEDRA 🪨
[1] PAPEL 📜
[2] TESOURA ✂️\033[0;0m'''))
player  = int(input('\033[1;36mFaça sua jogada: '))
print('\033[1;31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!\033[0;0m')
sleep(1)
print('\033[0;32m-=\033[0;0m'*11)
print('\033[1;36mO computador jogou {}'.format(itens[computador]))
print('O player jogou {}\033[0;0m'.format(itens[player]))
print('\033[0;32m-=\033[0;0m'*11)

if computador == 0:
    if player == 0:
        print(emoji.emojize('\033[1;31mEMPATE :confounded_face:', language='en'))
    elif player == 1:
        print(emoji.emojize('\033[1;31mO jogador VENCEU!:grinning_face_with_smiling_eyes:', language='en'))
    elif player == 2:
        print(emoji.emojize('\033[1;31mO jogador PERDEU!:disappointed_face:', language='en'))
    else:
        print('\033[1;31mJOGADA INVÁLIDA!!')
elif computador == 1:
    if player == 0:
        print(emoji.emojize('\033[1;31mO jogador PERDEU!:disappointed_face:', language='en'))
    elif player == 1:
        print(emoji.emojize('\033[1;31mEMPATE :confounded_face:', language='en'))
    elif player == 2:
        print(emoji.emojize('\033[1;31mO jogador VENCEU!:grinning_face_with_smiling_eyes:', language='en'))
    else:
        print('\033[1;31mJOGADA INVÁLIDA!!')
elif computador == 2:
    if player == 0:
        print(emoji.emojize('\033[1;31mO jogador VENCEU!:grinning_face_with_smiling_eyes:', language='en'))
    elif player == 1:
        print(emoji.emojize('\033[1;31mO jogador PERDEU!!:disappointed_face:',language='en'))
    elif player == 2:
        print(emoji.emojize('\033[1;31mEMPATE :confounded_face:',language='en'))
    else:
        print('\033[1;31mJOGADA INVÁLIDA!!')
        #isso deu MUITO trabalho, preciso aprender como importar biblioteca de cores e só digitar RED+'...' reset+ '...'
        #também se tem um modo mais prático para lidar com esses emojis