'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
prod = float(input('Qual o valor do produto em: R$'))
pag = int(input('[1]À vista (dinheiro ou cheque)\n[2]Cartão débito\n[3]2x no cartão\n[4]Acima de 3x no cartão\n'))
cash = prod - (prod * 10 / 100)
debito = prod - (prod * 5 / 100)
div2 = prod
div3 = prod + (prod * 30 / 100)
if pag == 1:
    print('O valor do produto é R${:.2f} e em dinheiro ou cheque tem um desconto de 10% e fica em R${:.2f} '.format(prod,cash))
elif pag == 2:
    print('O valor do produto é R${:.2f} e no cartão de débito com desconto de 5% fica em R${:.2f}'.format(prod,debito))
elif pag == 3:
    print('O valor do produto é R${:.2f} e em até 2x no cartão de crédito não há desconto!'.format(prod,div2)) #agora vi que nao precisava da variável div 2, era só colocar novamente o preço do produto
elif pag == 4:
    print('O valor do produto é R${:.2f} e em 3x ou mais no cartão há um acréscimo de 30%, o preço vai para R${:.2f}'.format(prod,div3))
else:
    pag = prod
    print('\033[0;30;41mOpção inválida\033[m') #fundo vermelho na mensagem de erro
# o professor usou print('{=^40}'.format(Nome loja)) # isso foi aprendido na aula de cores
# o menu usado por ele foi bem interessante, ele usou print  e tres aspas :
# print (''' ''') dessa forma ele pode dar enter e criar o menu sem o \n
#lembrando que eu nao precisava ter criado as variaveis com as funçoes, poderia ter colocado elas no if e encurtar o código
