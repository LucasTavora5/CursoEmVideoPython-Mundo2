'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''
from datetime import date
nascimento = int(input('Informe seu ano de nascimento para ser alocado a uma categoria: '))
anoatual = date.today().year
idade = anoatual - nascimento
print('O atleta nasceu em {} e sua idade atual é {}'.format(nascimento,idade))
if idade <=9 :
    print('Crianças até 9 anos de idade fazem parte da categoria MIRIM!')
elif idade > 9 and idade <=14:
    print('Crianças de 10 a 14 anos fazem parte da categoria INFANTIL!')
elif idade > 14 and idade <=19:   # quando chego no elif, posso usar direto <=19... pois se se a condição nao foi confirmada antes, ele passa pro proximo elif, nao necessitava do "and"
    print('Adolescentes com 15 anos ou adultos com até 19 anos fazem parte da categoria JÚNIOR!')
elif idade >19 and idade <= 25:
    print('Adultos de 19 a 25 anos fazem parte da categoria SÊNIOR!')
elif idade > 25:
    print('Adultos com mais de 25 anos fazem parte da categoria MASTER!')