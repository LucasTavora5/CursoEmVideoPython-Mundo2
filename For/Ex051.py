#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
p = int(input('Primeiro termo: ')) #primeiro número a aparecer
r = int(input('Razão: ')) #pluar de x em x
d = p+(10-1) *r #primeiro +10 depois ele -1 = 10 números pra aparecer * a razão que determina de quantos em quantos////essa linha foi complicada de pensar
for c in range(p,d+r,r): #vai contar do primeiro, da razão ao décimo,pulando de razão em razão
    print('{}'.format(c))