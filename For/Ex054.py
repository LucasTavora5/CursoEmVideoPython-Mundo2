'''Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year #declarando o ano atual
totmaior= 0 #contador
totmenor= 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu?: '.format(c))) #print dentro do contador, vai perguntar x vezes
    idade = atual-nascimento
    if idade>= 18:
        totmaior+= 1 #conta mais 1 pra cada pessoa maior
    else:
        totmenor += 1 #conta mais 1 pra cada pessoa menor
print('Temos {} pessoas maior de idade'.format(totmaior)) #print fora do laço só imprime 1x
print('Temos {} pessoas menor de idade'.format(totmenor))