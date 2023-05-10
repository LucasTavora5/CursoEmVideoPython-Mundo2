'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
if (n1 + n2) / 2 < 5:
    print('REPROVADO')
elif (n1 + n2) / 2 == 5 or (n1 + n2)/2 <= 6.9:
    print('RECUPERAÇÃO')
elif (n1 + n2) / 2 >= 7:
    print('APROVADO')
    #eu poderia também criar a variável média em vez de criar essa função no if, ficaria mais limpo e eu poderia usar o .format com a média
