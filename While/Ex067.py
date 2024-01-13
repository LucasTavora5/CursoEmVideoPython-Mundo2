'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.'''


while True:
    n1 = int(input('Insira um número para obter sua tabuada(número negativo para parar): '))
    if n1 <0:
        break
    for c in range (1,11):
        print(f'{n1} x {c} = {n1*c}')
print('Programa finalizado')

