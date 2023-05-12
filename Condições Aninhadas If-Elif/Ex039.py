'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

'''idade = int(input('Informe sua idade: '))
if idade == 17:
    print('Falta pouco tempo pra você se alistar, confira o prazo de inscrição!')
elif idade < 16:
    print('Você ainda é muito novo para se alistar!')

elif idade == 18:
    print("Você já pode se alistar, confira o prazo de inscrição!")
elif idade > 18:
    print('Já passou o prazo do seu alistamento, voce deveria ter se alistado há {} ano(s)'.format(idade-18))
'''
from datetime import date
anoatual = date.today().year # usando o date time com o ano atual
datanascimento = int(input('Informe seu ano de nascimento: '))
idade = anoatual-datanascimento
print('Quam nasceu em {} tem {} anos em {}'.format(datanascimento,idade,anoatual))
if idade == 18:
    print('Você deve se alistar esse ano, confira o prazo de inscrição!!!')
elif idade == 17:
    print('Você que é jovem e completa 18 anos esse ano, confira o prazo de inscrição')
elif idade <18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) pro alistamento!'.format(saldo))

elif idade > 18:
    saldo = idade - 18
    print('já passaram {} anos desde o seu  alistamento'.format(saldo))

'''Essa forma que o professor fez foi muito bacana, ele fez o uso do datetime para comparar o ano de nascimento
com o ano atual e gerar a diferença para achar a idade.Muito criativo, preciso pensar fora da caixa!!!!'''