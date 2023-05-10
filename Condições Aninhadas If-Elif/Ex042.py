'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
r1 = float(input('Informe o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Informe o terceiro segmento: ')) #uso de 02 if, o primeiro obrigatoriamente será atendido, o segundo também, porém se nao for, então passar pra proxima etapa...
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM formar um triângulo ', end='') #uso do end fará com que após essa frase seja usada, use ao lado a do próximo print
    if r1 == r2 == r3:
         print('EQUILÁTERO!')
    elif r1 != r2 != r3 !=r1: # se eu nao colocar que o r3 também é diferente de r1, ele nao entende que são TODOS os lados diferentes
         print('ESCALENO!')
    else:
         print('ISÓSCELES!') # se nao atender nem um nem outro, quer dizer que nao sao 3 iguais, nem 3 diferentes, são apenas 2 iguais