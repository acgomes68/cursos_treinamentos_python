'''
Modos possíveis:
r - (read) somente leitura (default). Necessário que o arquivo já exista
w - (write) escrita sobrepondo o conteúdo existente. Cria o arquivo caso não exista
r+ - (read/write) leitura e escrita. Necessário que o arquivo já exista
a - (append) escrita completando o conteúdo existente. Cria o arquivo caso não exista
b - (binary) abertura de arquivo binário. Necessário que o arquivo já exista
rb - (read/binary) leitura de arquivo binário. Necessário que o arquivo já exista
'''
# Criar e abrir arquivo no modo escrita
arquivo = open('arquivo.txt', 'w')

# Escrever conteúdo no arquivo
arquivo.write('Versão 1!\n')
arquivo.write('Olá, pessoal!\n')

# Fechar arquivo
arquivo.close()

# Abrir arquivo no modo leitura
arquivo = open('arquivo.txt', 'r')

# Exibir conteúdo do arquivo
print(arquivo.read())

# Fechar arquivo
arquivo.close()

# Criar e abrir arquivo no modo escrita sobrepondo conteúdo anterior
arquivo = open('arquivo.txt', 'w')

# Escrever conteúdo no arquivo
arquivo.write('Versão 2!\n')

# Escrever conteúdo no arquivo
for i in range(1000):
    arquivo.write('Número: ' + str(i) + '\n')

# Fechar arquivo
arquivo.close()

# Abrir arquivo no modo leitura
arquivo = open('arquivo.txt', 'r')

# Exibir conteúdo do arquivo
print(arquivo.read())

# Fechar arquivo
arquivo.close()

# Abrir arquivo no modo escrita completando conteúdo anterior
arquivo = open('arquivo.txt', 'a')

# Obtém o valor ascii da letra A
valor_ascii_a = ord('A')

# Escrever conteúdo no arquivo
arquivo.write('Versão 3!\n')

# Escrever conteúdo no arquivo
for i in range(26):
    arquivo.write('Letra: ' + chr(valor_ascii_a + i) + '\n')

# Fechar arquivo
arquivo.close()

# Abrir arquivo no modo leitura
arquivo = open('arquivo.txt', 'r')

# Exibir conteúdo do arquivo
print(arquivo.read())

# Fechar arquivo
arquivo.close()

# Criar e abrir arquivo no modo escrita sobrepondo conteúdo anterior
arquivo = open('arquivo.txt', 'w')

# Escrever conteúdo no arquivo
arquivo.write('Versão 4!\n')
arquivo.write('Tchau, pessoal!\n')

# Fechar arquivo
arquivo.close()

# Abrir arquivo no modo leitura
arquivo = open('arquivo.txt', 'r')

# Exibir conteúdo do arquivo
print(arquivo.read())

for linha in arquivo:
    print(linha)

# Fechar arquivo
arquivo.close()

# Abrir arquivo no modo bináro
arquivo = open('acgomes_avatar.jpeg', 'rb')

# Exibir conteúdo do arquivo
print(arquivo.read())
