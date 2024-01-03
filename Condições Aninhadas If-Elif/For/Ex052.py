#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n1 = int(input('Digite um número para saber se ele é um número PRIMO: '))
total = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        total += 1
    else:
        print('{}'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes'.format(n1,total))
if total == 2:
    print('\nEsse é um número PRIMO!!')
else:
        print('\nEsse NÃO é um número PRIMO')  #esse foi o mais dificil até agora, nao acho que FOR seja uma boa opção pra resolver isso

