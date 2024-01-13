'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

n1 = 0
s = 0
cont = 0            #iniciando variáveis
while n1 != 999:
    n1 = int(input('Digite um número (999 para parar): ')) #insira números enquanto o mesmo for diferente de 999
    if n1 == 999:
       break                                                   #se for 999 pausa
    cont += 1                                                  #contador de inserção
    s += n1                                                    #soma de input
print(f'Você inseriu {cont} números e a soma deles é: {s}')
