'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('Gerador de PA!!')
print('=='*10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Insira a razão: '))
termo = n1
cont = 1
while cont <=10:
    print(f'{termo},', end='')
    termo+=razao
    cont+=1
print('FIM')