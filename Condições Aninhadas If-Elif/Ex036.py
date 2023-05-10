''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valorcasa = float(input('Insira o valor da casa:R$'))
salario = float(input('Insira seu salário mensal:R$'))   #variáveis
anos = int(input('Em quantos anos deseja pagar?  '))
prestacao = valorcasa / (anos*12)  #valor da casa dividido pela quantidade de anos * 12 meses
print('Para comprar uma casa no valor de R${:.2f} em {} anos o valor da prestação será R${:.2f}'.format(valorcasa,anos,prestacao))
if prestacao > salario*30/100:    #Condicional dos 30% do salário
    print('O valor da prestação excede 30% do seu salário, empréstimo NEGADO!')

else :
    print('é possível fazer negócios!!!')

'''na aula ele usa end = ' ' 
 O argumento end especifica o caractere que deve ser usado para encerrar a saída de texto durante a impressão. 
 Por padrão, o valor de end é um caractere de nova linha ('\n'), 
 o que significa que cada chamada para print() termina com uma nova linha.
 print("Olá", end=' ')
 print("Mundo")
 Olá Mundo
 o que faz com que a próxima chamada para print() comece a imprimir a partir do espaço em branco, em vez de uma nova linha.
  Dessa forma, a palavra "Mundo" é impressa logo após o espaço, resultando em "Olá Mundo".'''