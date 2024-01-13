'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

c = 0
soma = 0
n1 = int(input('Digite um número (ou 999 para parar): '))

while n1 != 999:
    soma += n1
    c += 1  # Contar quantos números foram digitados
    n1 = int(input('Digite um número (ou 999 para parar): '))

print(f'Foram digitados {c} números e a soma deles é: {soma}')