# Define uma lista de nomes
nomes = ['Guilherme', 'João', 'Marcelo', 'Antonio']

# Exibe cada nome da lista
for nome in nomes:
    print(nome)

# Cria uma lista com 5 números (0 a 4)
lista_numeros = range(5)

# Exibe cada número da lista
for item in lista_numeros:
    print(item)

# Cria uma lista com 5 números iniciando no 5 (5 a 9)
lista_numeros = range(5, 10)

# Exibe cada número da lista
for item in lista_numeros:
    print(item)

# Cria uma lista com 5 números iniciando no 5 (5 a 9)
lista_numeros = range(0, 100, 2)

# Exibe cada número da lista
for item in lista_numeros:
    print(item)

# Exibe cada número da lista
for item in range(0, 100, 2):
    print(item)

# Exibe cada número da lista
for i in range(4):
    print(nomes[i])

# Exibe cada número da lista
for i in range(len(nomes)):
    print(nomes[i])

palavra = 'Antonio Gomes'
for letra in palavra:
    print(letra)

i = 0
while (i < 10):
    print('i ainda é menor que 10: ', i)
    i += 1

print('Acabou o while: ', i)

