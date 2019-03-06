'''
API: OMDb API: web service gratuita para consulta de filmes
'''
import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('https://www.omdbapi.com/?t=' + titulo + '&type=movie&apikey=25ecba7b')
        dicionario = json.loads(req.text)
        return dicionario
    except Exception as e:
        print('Erro de acesso a API OMDb: ', e)
        return None

def exibir_detalhes(op, filme):
    # {'Language': 'English, Swedish', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg', 'Production': 'Paramount Pictures', 'Response': 'True', 'Released': '19 Dec 1997', 'Country': 'USA', 'BoxOffice': 'N/A', 'Plot': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.', 'Title': 'Titanic', 'DVD': '10 Sep 2012', 'Ratings': [{'Value': '7.8/10', 'Source': 'Internet Movie Database'}, {'Value': '89%', 'Source': 'Rotten Tomatoes'}, {'Value': '75/100', 'Source': 'Metacritic'}], 'Awards': 'Won 11 Oscars. Another 111 wins & 77 nominations.', 'Runtime': '194 min', 'Rated': 'PG-13', 'Website': 'http://www.titanicmovie.com/', 'imdbID': 'tt0120338', 'Writer': 'James Cameron', 'Actors': 'Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates', 'imdbVotes': '934,048', 'imdbRating': '7.8', 'Director': 'James Cameron', 'Type': 'movie', 'Year': '1997', 'Genre': 'Drama, Romance', 'Metascore': '75'}
    if filme is not None and filme['Response'] != 'False':
        print('Título: ', filme['Title'])
        print('Ano: ', filme['Year'])
        print('Idioma: ', filme['Language'])
        print('Diretor: ', filme['Director'])
        print('Atores: ', filme['Actors'])
        print('Nota: ', filme['imdbRating'])
        print('Prêmios: ', filme['Awards'])
        print('Poster: ', filme['Poster'])
    else:
        print('Filme {} não encontrado' . format(op))


sair = False
while not sair:
    op = input('Digite o nome do filme a pesquisar ou <ENTER> para sair: ')
    if op.strip() == '':
        print('Saindo...')
        sair = True
    else:
        filme = requisicao(op)
        exibir_detalhes(op,filme)
