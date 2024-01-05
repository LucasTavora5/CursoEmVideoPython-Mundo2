'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''
for num in range(0, 51): #51 pra incluir o 50
    if num % 2 == 0 : # se o número dividido por 2 tiver resto 0, ele é par!!
        print(num) #como está indentado dentro do if, ele só vai imprimir o que tiver imposto na condição

#for num in range(2, 51, 2) # isso também funcionaria e iria direto ao ponto