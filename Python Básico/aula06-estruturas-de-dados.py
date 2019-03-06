# Estrutura de dados - Coleções

# Inicializa uma lista
print('# Inicializa uma lista')
minha_lista = []

# Inicializa uma tupla
print('# Inicializa uma tupla')
minha_tupla = ()

# Inicializa um dicionário
print('# Inicializa um dicionário')
meu_dicionario = {}
# OU
# meu_dicionario = dict()


# Inicializa um conjunto
print('# Inicializa um conjunto')
meu_conjunto = set()

# Define uma lista (list) de nomes: Coleção dinâmica de itens (pode ordenar, adicionar ou remover)
print('\n# Define uma lista (list) de nomes')
minha_lista = ['Guilherme', 'João', 'Marcelo', 'Antonio']

# Define uma tupla (tuple) de nomes: Coleção estática de itens (não adiciona, nem remove)
print('# Define uma tupla (tuple) de nomes')
minha_tupla = ('Guilherme', 'João', 'Marcelo', 'Antonio')

# Define um dicionário (dict) de nomes: Coleção dinâmica do tipo chave:valor
print('# Define um dicionário (dict) de nomes')
meu_dicionario = {'nome': 'Guilherme', 'idade': 27}

# Define um conjunto (set) de nomes: Coleção dinâmica sem repetição, sem chave e sem ordenação
print('# Define um conjunto (set) de nomes')
meu_conjunto = {'Guilherme', 'João'}

# Busca em lista
print('\n# Busca em lista')
if 'Guilherme' in minha_lista:
    print('Guilherme está na lista')
else:
    print('Guilherme NÃO está na lista')

# Busca em tupla
print('\n# Busca em tupla')
if 'Guilherme' in minha_tupla:
    print('Guilherme está na tupla')
else:
    print('Guilherme NÃO está na tupla')

# Busca em dicionário
print('\n# Busca em dicionário')
if 'Guilherme' in meu_dicionario.values():
    print('Guilherme está no dicionário')
else:
    print('Guilherme NÃO está no dicionário')

# Busca em conjunto
print('\n# Busca em conjunto')
if 'Guilherme' in meu_conjunto:
    print('Guilherme está no conjunto')
else:
    print('Guilherme NÃO está no conjunto')

# Loop em lista
print('\n# Loop em lista')
for valores in minha_lista:
    print(valores)

# Loop em tupla
print('\n# Loop em tupla')
for valores in minha_tupla:
    print(valores)

# Loop em dicionário
print('\n# Loop em dicionário')
for valores in meu_dicionario.values():
    print(valores)

# Loop em conjunto
print('\n# Loop em conjunto')
for valores in meu_conjunto:
    print(valores)

# Alteração de valor em lista
print('\n# Alteração de valor em lista')
print(minha_lista)
minha_lista[0] = 'Renata'
print(minha_lista)

# Alteração de valor em tupla
print('\n# Alteração de valor em tupla')
# NÃO PERMITIDO
print('# NÃO PERMITIDO')

# Alteração de valor em dicionário
print('\n# Alteração de valor em dicionário')
print(meu_dicionario)
meu_dicionario['nome'] = 'João'
print(meu_dicionario)

# Alteração de valor em conjunto
print('\n# Alteração de valor em conjunto')
# NÃO PERMITIDO
print('# NÃO PERMITIDO')

# Inclusão de valor em lista
print('\n# Inclusão de valor em lista')
print(minha_lista)
minha_lista.append('Maria')
print(minha_lista)

# Inclusão de valor em tupla
print('\n# Inclusão de valor em tupla')
# NÃO PERMITIDO
print('# NÃO PERMITIDO')

# Inclusão de valor em dicionário
print('\n# Inclusão de valor em dicionário')
print(meu_dicionario)
meu_dicionario['endereco'] = 'Rua João das Neves, 214'
meu_dicionario['telefone'] = '(55) 4566-2398'
print(meu_dicionario)

# Inclusão de valor em conjunto
print('\n# Inclusão de valor em conjunto')
print(meu_conjunto)
meu_conjunto.add('Maria')
print(meu_conjunto)

# Exclusão de valor em lista
print('\n# Exclusão de valor em lista')
print(minha_lista)
minha_lista.remove('Maria')
print(minha_lista)

# Exclusão de valor em tupla
print('\n# Exclusão de valor em tupla')
# NÃO PERMITIDO
print('# NÃO PERMITIDO')

# Exclusão de valor em dicionário
print('\n# Exclusão de valor em dicionário')
print(meu_dicionario)
meu_dicionario.pop('idade')
print(meu_dicionario)

# Exclusão de valor em conjunto
print('\n# Exclusão de valor em conjunto')
print(meu_conjunto)
meu_conjunto.remove('Maria')
print(meu_conjunto)

# Combinação de coleções
print('\n# Combinação de coleções')
loucura = [(1, 2), (3, 4), (5, 6), ({'joao', 'maria'}, {'gabriel'})]
print(loucura)

'''
Docs do Phyton 3.5: https://docs.python.org/3.5/
Docs do Phyton 2.7: https://docs.python.org/2.7/
'''
