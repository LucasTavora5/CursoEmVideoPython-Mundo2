#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {}º número:'.format(c))) #primeira vez usando .format no input, o laço For me possibilita x inputs e funciona de forma crescente ou decrescente
    if num % 2 == 0:
        soma += num #soma com o prox número se for par
        cont += 1 #conta todos os números de 1 em 1 se forem par
print('Voce inserriu {} números pares e a soma entre eles é {}'.format(cont, soma))



