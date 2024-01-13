'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
resposta = 'S'
soma = quant = media = 0
maior = menor = 0
while resposta in 'Ss':
    n1 = int(input('Digite um número:'))
    soma += n1
    quant += 1
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print(f'A quantidade de números foi {quant} e média dos valores é: {media} ')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')