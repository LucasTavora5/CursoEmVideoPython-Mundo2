'''Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

n1 = int(input('Insina um número inteiro qualquer: '))
escolha = int(input('Escolha as opções de conversão: \n[1]Binário\n[2]Octal\n[3]Hexadecimal\nOpção: '))#criei esse painel de escolha simples usando \n, espero aprender mais tecnicas futuramente
b = bin(n1)
o = oct(n1)   #o Python me gera as funçoes de binário,octal e hexadecimal
h = hex(n1)
if escolha == 1:
    print('O número {} convertido para binário se torna  {}'.format(n1,b[2:])) #em vez de criar variaveis, eu poderia ter chamado os métodos no .format
elif escolha == 2:
    print('O número {} convertido para Octal se torna  {}'.format(n1,o[2:]))#quando uso colchetes, eu consigo fatiar as posições,logo [2:] quer dizer que vai ler do segundo digito em diante, o que vem depois do ":" determina o fim
    
elif escolha == 3:
    print('O número {} convertido para hexadecimal se torna  {}'.format(n1,h[2:]))
else:
    print('Esse valor não é uma opção, reinicie o programa!') #usando as condições aninhadas