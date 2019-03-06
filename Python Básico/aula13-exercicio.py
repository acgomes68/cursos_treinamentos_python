'''
API: OMDb API: web service gratuita para consulta de filmes
'''
import requests
import json

def pesquisa_filmes(titulo):
    lista = None
    lista_titulos = []
    indice = 1

    print('Aguarde, buscando lista de filmes...')

    try:
        req = requests.get('https://www.omdbapi.com/?s=' + titulo + '&type=movie&apikey=25ecba7b')
        lista = json.loads(req.text)
    except Exception as e:
        print('Erro de acesso a API OMDb: ', e)
        return lista_titulos

    if lista is not None and lista['Response'] != 'False':
        qtd_filmes = lista['totalResults']
        qtd_paginas = int(qtd_filmes) / 10
        if int(qtd_filmes) % 10 != 0:
            qtd_paginas += 2

        qtd_paginas = int(qtd_paginas)

        for filme in lista['Search']:
            lista_titulos.append({'id': filme['imdbID'], 'titulo': filme['Title'], 'ano': filme['Year']})
            print('Encontrado {} filme(s): {}' . format(str(indice), filme['Title'] + '(' + filme['Year'] + ')'))
            indice += 1

        for i in range(2, qtd_paginas):
            req = requests.get('https://www.omdbapi.com/?s=' + titulo + '&type=movie&page=' + str(i) + '&apikey=25ecba7b')
            lista = json.loads(req.text)

            for filme in lista['Search']:
                lista_titulos.append({'id': filme['imdbID'], 'titulo': filme['Title'], 'ano': filme['Year']})
                print('Encontrado {} filme(s): {}'.format(str(indice), filme['Title'] + '(' + filme['Year'] + ')'))
                indice += 1

    return lista_titulos

def exibir_detalhes(lista, indice_filme):
    titulo_filme = lista[indice_filme]['titulo']
    try:
        req = requests.get('https://www.omdbapi.com/?t=' + titulo_filme + '&type=movie&apikey=25ecba7b')
        filme = json.loads(req.text)
        print('Item: ', indice_filme + 1)
        print('Título: ', filme['Title'])
        print('Ano: ', filme['Year'])
        print('Idioma: ', filme['Language'])
        print('Diretor: ', filme['Director'])
        print('Atores: ', filme['Actors'])
        print('Nota: ', filme['imdbRating'])
        print('Prêmios: ', filme['Awards'])
        print('Poster: ', filme['Poster'])
    except Exception as e:
        print('Erro de acesso a API OMDb: ', e)

sair = False
while not sair:
    op = input('Digite o nome do filme ou parte dele para pesquisar ou <ENTER> para sair: ')
    if op.strip() == '':
        print('Saindo...')
        sair = True
    else:
        lista = pesquisa_filmes(op)
        if (len(lista) > 0):
            indice_filme = 0
            while indice_filme != '':
                print()
                indice_filme = input('Digite o número do filme para obter maiores detalhes ou <ENTER> para retornar: ')
                if indice_filme.strip() != '':
                    indice_filme = int(indice_filme)
                    if indice_filme > 0 and indice_filme <= len(lista):
                        exibir_detalhes(lista, indice_filme - 1)
        else:
            print('Nenhum filme encontrado que possua {} no título '.format(op))


