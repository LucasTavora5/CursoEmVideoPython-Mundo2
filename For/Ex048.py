'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
s = 0 #soma
c = 0 #contador
for num in range(1,500,2):
    if num %3 ==0: #condicional para ser mútiplo de 3
        s += num
        c += 1 #lembrando que += voce soma a variável + ela mesmo   
print('Existem {}  multiplos de 3 até 500 é {}'.format(c,s)) #achei interessante como a identação atua, se eu der tab nessa linha, ele mostra a soba de TUDO