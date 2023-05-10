'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''
#tentarei fazer algo mais interativo, com mensagem de início
print('Esse é seu programa de Índice de massa corporal (IMC), basta seguir as instruções para saber seu resultado!!!')
altura = float(input('Informe sua altura em metros: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura ** 2)
print('Com {}m de altura e {} kg, você tem um IMC de {:.1f}, isso indica que você está '.format(altura,peso,imc),end='') #uso do end para complementar esse print com o proximo
if imc < 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('No peso ideal!')
elif imc <= 30:
    print('Com sobrepeso!')
elif imc <= 40:
    print('Obeso!')
elif imc > 40:
    print('Com obesidade mórbida!')