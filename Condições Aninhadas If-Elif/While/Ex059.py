'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
while True:
    #solicitar valor ao usuário
    n1 = float(input('Informe o primeiro valor: '))
    n2 = float(input('Informe o segundo valor: '))
    #mostrar painel de opções
    print('\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa')
    opcao = int(input('Qual operação deseja realizar: '))
    #realizar opção diacordo com escolha do usuário
    if opcao == 1:
        resultado = n1 + n2
        print(f'A soma entre os números {n1} e {n2} é: {resultado}')
    elif opcao == 2:
        resultado = n1 * n2
        print(f'A multiplicação entre os números {n1} e {n2} é: {resultado}')
    elif opcao == 3:
        resultado = max(n1,n2)
        print(f'O maior número entre {n1} e {n2} é: {resultado}')
    elif opcao == 4:
        continue #reinicia o loop para obter novos números
    elif opcao == 5:
        print('Programa encerrado, até logo!')
        break #encerra o loop
    else:
        print('Opção inválida!')