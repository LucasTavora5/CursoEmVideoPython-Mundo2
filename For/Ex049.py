#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
t = int(input('Insira um número para saber sua tabuada: '))
for num in range(1, 11):
    print('{}x{}={}'.format(t,num,t*num))