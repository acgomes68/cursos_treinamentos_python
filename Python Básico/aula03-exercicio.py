'''
Exercício:
Faça um programa que pergunte a idade, o peso e altura de uma pessoa e decide se ela está apta a ser do Exército.
Para entrar no exército é preciso ter mais de 18 anos, pesar mais ou igual a 60Kg e medir mais ou igual a 1.70m
'''

print('Seleção para o Exército:')

idade = int(input('Digite sua idade: (>18 anos) '))
peso = float(input('Digite seu peso: (>=60Kg) '))
altura = float(input('Digite sua altura: (>=1.70) '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Parabéns! Você está apto para o Exército.')
else:
    print('Lamento! Mas você não está apto para o Exército.')
