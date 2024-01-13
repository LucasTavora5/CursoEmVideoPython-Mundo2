'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
print('Gerador de PA!!')
print('=='*10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Insira a razão: '))
termo = n1
cont = 1
total=0
mais=10
while mais !=0:
    total+=mais
    while cont <=total:
        print(f'{termo},', end='')
        termo+=razao
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos no total')