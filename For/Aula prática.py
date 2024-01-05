'''for c in range (0,6): #o nome C é só um exemplo, pode ser qualquer coisa, se eu printar o C,ele conta de x a y
    print('Oi') #esse oi está dentro do laço de repetição, já o "FIM" está fora, entao nao será repetido
print('FIM') # atenção na indentação!
for c in range (6,0, -1):
dessa forma ele conta ao contrário, o terceiro número depois da vírgula é a iteração
(0, 7, 2) ele conta de 1 a 6 pulando de 2 em 2'''

'''n = int(input('Digite um número: '))
for c in range(0,n+1): # preciso colocar esse +1,pois ele conta até o npumero anterior
    print (c) #como estou interagindo com uma sequencia numérica, ao dar print C, ele conta a numeração no range dos parenteses (x, y+1)
print('FIM')
i = int(input('Início: ')) #de onde quero começar a andar com o avatar?
f = int(input('Fim: '))#até qual casa?
p = int(input('Passo: '))# de quantos em quantos passos?
for c in range(i, f+1):
    print(c)
for c in range(0,10): #aqui ele vai me pedir pra digitar um número 10 vezes, isso parece ser muito útil!!!!!
    print('Digite um número: ')
print('FIM')
'''
s = 0 #declaramos uma variavel S com valor inicial 0
for c in range(0,4): #aqui ele vai me pedir pra "digitar um valor" 4x (0,4)!!!!!
    n = int(input('Digite um valor: '))
    s+=n # A cada vez que eu adiciono um N, ele soma  e substitui o valor de S,EX.: s=0 n=10, logo s=10 +n=x(10), logo, s=20 +n =x(10),logo s=30...
print('A soma dos 4 valores é {}'.format(s))