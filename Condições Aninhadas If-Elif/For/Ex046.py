'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep # usei sleep da biblioteca Time pra fazer a pausa de 1s
for c in range(10, -1, -1): #-1 fazendo a iteração e dizendo ao python pra minuir 1 até chegar a 0, o outro -1 é pra ele contar o 0 como pedido no enunciado
    sleep(1)
    print(c)
print('Feliz ano novo!!!!!!!!')