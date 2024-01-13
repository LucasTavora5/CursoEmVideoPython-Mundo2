'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
v = d = 0
while True:
    n1 = int(input('Insira um número PAR ou ÍMPAR para jogar contra a máquina!: '))
    comp = randint(0,10)
    total = n1 + comp
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {n1}  e o computador {comp}. total de  {total}')
    if tipo == 'P':
        if total %2 == 0:
            print('Você ganhou!')
            v+=1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 !=0:
            print('Você ganhou!')
            d+=1
        else:
            print('Você perdeu!')
            break
print(f'Você venceu {v} vezes!')