print('Hello World!\nSegundo print')

nome = 'Antonio'
idade = 50
altura = 1.72
#dtNascimento = 09/08/1968

tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)

print(nome)
print(idade)
print(altura)
print(tipo_nome)
print(tipo_idade)
print(tipo_altura)

print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura')

nome = input('Escreva seu nome: ')
idade = input('Qual a sua idade: ')
altura = input('Qual a sua altura: ')

print(nome, 'tem', idade, 'anos e', altura, 'de altura')

numero1 = 4
numero2 = 16

potenciacao = numero1 ** 2 # Elevado à segunda potência
raiz_quadrada = numero2 ** (1/2) # Raiz quadrada

print(numero1, 'elevado a segunda potência é igual a', potenciacao)
print('a raiz quadrada de', numero2, 'é igual a', raiz_quadrada)

'''
EXERCÍCIO: Faça um formulário que pergunte o nome, cpf, endereco, idade, altura e telefone
e imprima isso em um relatório organizado
'''

