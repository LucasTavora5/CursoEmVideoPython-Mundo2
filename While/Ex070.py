'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
tot_compra = tot_comprak = menor_preco = cont= 0
barato = ' '
while True:
    nome_prod = str(input('Nome do produto: '))
    preco_prod = float(input('Preço do produto: '))
    cont+=1
    tot_compra += preco_prod
    if preco_prod > 1000:
        tot_comprak +=1
    if cont == 1:
        menor_preco = preco_prod
        barato = nome_prod
    else:
        if preco_prod < menor_preco:
            menor_preco = preco_prod
            barato = nome_prod
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'o valor total da compra foi :{tot_compra:.2f}')
print(f'{tot_comprak :.2f} produtos custam mais de R$1000,00 !')
print(f'O iten mais barato foi "{barato}" e custa R${menor_preco:.2f}')