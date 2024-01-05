''' Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
import random
computer_number = random.randint(0, 10)
your_number = int(input('Choose  a number between 0 and 10: '))
guesses = 1
while your_number != computer_number:
    your_number = int(input('Woops, Wrong number. Try again: '))
    guesses +=1 # aqui estou incrementando o contador a partir da primeira tentativa

print(f'Congratulations! The right number is {computer_number}, you got it in {guesses} guesses.')

'''Eu poderia ter feito esse programa de forma mais dinâmica com usando condicionais e mostrando mais mensagens
como por exemplo se o jogador está perto ou longe de acertar'''