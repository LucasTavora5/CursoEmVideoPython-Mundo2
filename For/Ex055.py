'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
contmaior = 0
contmenor = 0
for c in range(1, 6):
    kg = float(input('Peso da  {}ª pessoa: '.format(c)))
    if c == 1:
        contmenor = kg
        contmaior = kg
    else:
        if kg > contmaior:
            contmaior = kg
        if kg < contmenor:
            contmenor = kg
print('O menor peso  foi de {}Kg'.format(contmenor))
print('O maior peso foi de {}Kg'.format(contmaior))

'''Declarei 02 contadores valendo 0, um input dentro do laço FOR pra perguntar 5x
condicional: SE c for igual 1 (o primeiro peso), ele se torna o maior e o menor peso ao mesmo tempo
SENÃO, FAÇA: SE o Kg do imput for MAIOR que cont maior(peso anterior), cont maior é igual KG(passa a ser o maior)
SE kg for MENOR que contmenor(menor peso anterior, cont menor é = a kg (passa a ser o menor)
dessa forma consigo comparar e saber qual é o maior ou menor dos 5 pesos'''