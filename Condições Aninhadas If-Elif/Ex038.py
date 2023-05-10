'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''
n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))
if n1>n2:
    print('O número {} é MAIOR que o número {}'.format(n1,n2))
elif n1<n2:
    print('O número {} é MENOR que o número {}'.format(n1,n2))
else:
    print('Os número {} e o número {} são iguais!!!'.format(n1,n2)) #Não coloquei outro Elif com ''=='' pois se nao for nem maior nem menor são iguais