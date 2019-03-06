'''
Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso, o nome irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista
'''
lista_nomes = []
qtde_nomes = int(input('Quantos convidados para a festa? '))

i = 0
while (i < qtde_nomes):
    nome = input('Qual o nome para o convidado #{}: ' . format(i + 1))
    lista_nomes.append(nome.strip().capitalize())
    i += 1

print('Total de nomes: ', str(len(lista_nomes)))
print('Lista de Nomes')
print(lista_nomes)

for nome in lista_nomes:
    print(nome)

for i in range(qtde_nomes):
    nome = input('Qual o nome para o convidado #{}: '.format(i + 1))
    lista_nomes.append(nome.strip().capitalize())

print('Total de nomes: ', str(len(lista_nomes)))
print('Lista de Nomes')
print(lista_nomes)

for nome in lista_nomes:
    print(nome)