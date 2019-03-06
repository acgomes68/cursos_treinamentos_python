# Define conteúdo da string
frase = 'Oi, tudo bem?'

# Retorna a conteúdo da 5a. posição da string
print(frase[4])

# Retorna a conteúdo da 5a. até a 13a. posição da string
print(frase[4:12])

# Retorna a conteúdo da 5a. até a 13a. posição da string, alternando a cada 2 posições
print(frase[4:12:2])

# Define conteúdo da lista
lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']
print(lista_nomes)

# Adiciona elementos no final da lista
lista_nomes.append('Antonio')
lista_nomes.append('Renata')
print(lista_nomes)

# Exclui elemento da lista que corresponde ao conteúdo do parâmetro
lista_nomes.remove('Antonio')
print(lista_nomes)

# Insere elemento na 2a. posição da lista
lista_nomes.insert(1, 'Antonio')
print(lista_nomes)

# Substitui o valor do 1o. elemento da lista
lista_nomes[0] = 'Márcio'
print(lista_nomes)

# Adiciona elementos no final da listas
lista_nomes.append('João')
lista_nomes.append('João')
print(lista_nomes)

# Conta quantos elementos na lista correspondem ao conteúdo do parâmetro
print("lista_nomes.count('João'): {}" . format(lista_nomes.count('João')))

# Exibe o tamanho da string ou a quantidade de elementos da lista
print('len(frase): {}' . format(len(frase)))
print('len(lista_nomes): {}' . format(len(lista_nomes)))

# Retorna o conteúdo e exclui o último elemento da lista
lista_nomes.pop()
print(lista_nomes)
print("lista_nomes.count('João'): {}" . format(lista_nomes.count('João')))

# Retorna o conteúdo da string formatada para minúsculo
print(frase.lower())

# Retorna o conteúdo da string formatada para maiúsculo
print(frase.upper())

# Separa a string por um determinado caracter e retorna uma lista
frase_separada = frase.split(',')
print(frase_separada)
print(frase_separada[0])
print(frase_separada[1])

# Concatenação de strings
frase_nova = frase + ' Como vai você?'
print(frase_nova)
