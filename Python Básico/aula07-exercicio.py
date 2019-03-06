'''
Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior número dentro dessa coleção
faça outra que receb o menor número dessa coleção
'''

def maior_valor(colecao):
    return max(colecao)

def menor_valor(colecao):
    return min(colecao)

colecao = {27, 35, 18, 15, 87, 2}

print('Maior valor: {}' . format(maior_valor(colecao)))
print('Menor valor: {}' . format(menor_valor(colecao)))

