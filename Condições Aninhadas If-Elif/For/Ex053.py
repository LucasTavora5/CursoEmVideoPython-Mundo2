'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase: '))
palavras = frase.split() #separa a frase
junto = ''.join(palavras) #junta a frase pra virar uma palavra só
inverso = ''
for letras in range(len(junto)-1,-1,-1):#len pra pegar até a ultima palavra e vai ler da ultima-1, ate a primeira-1,contando ao contrário -1
    inverso += junto[letras] #aqui ele inverte o "junto" indo de x a y ao contrario
if inverso == junto: #depois de inverter as letras acima, se o inverso for igual a elas juntas, temos o palíndromo
    print('Você digitou "{}" o inverso é "{}", TEMOS UM PALÍNDROMO!'.format(frase, inverso))
else:
    print('Você digitou "{}" o inverso é "{}", NÃO temos um palíndromo!!'.format(frase, inverso))

#esse eu precisei acompanhar o vídeo, não consegui pensar em como inverter, quando descobri que era usando -1 ficou tudo muito claro