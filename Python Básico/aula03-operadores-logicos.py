# True ou False
# if: /elif: /else:
# Operadores: ==   !=  >   <   >=  <=
# Comparações: and  or  not
a = 2
b = 1

if a > b:
    print(a, 'é maior do que', b)
else:
    print(a, 'não é maior do que', b)

print('Menu\n1 - Escreve Antonio\n2 - Escreve João\n3 - Escreve Maria\n')

opcao = input('Escolha sua opção: ')

if opcao == '1':
    print('Antonio')
elif opcao == '2':
    print('João')
elif opcao == '3':
    print('Maria')
else:
    print('Opção inválida')

'''
Exercício:
Faça um programa que pergunte a idade, o peso e altura de uma pessoa e decide se ela está apta a ser do Exército.
Para entrar no exército é preciso ter mais de 18 anos, pesar mais de 60Kg e medir mais de 1.70m
'''