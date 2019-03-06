import oauth2
import json
import urllib.parse

class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        consumer = oauth2.Consumer(consumer_key, consumer_secret)
        token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(consumer, token)

    def tweet(self, novo_tweet):
        return self.executar_requisicao(novo_tweet, 'update')

    def search(self, query, lang='pt'):
        objeto = self.executar_requisicao(query, 'search', lang)
        return objeto['statuses']

    def executar_requisicao(self, conteudo, tipo_requisicao = 'search', lang = 'pt'):
        query_codificada = urllib.parse.quote(conteudo, safe='')

        if tipo_requisicao == 'search':
            endpoint = 'https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=' + lang
            verbo_http = 'GET'
        elif tipo_requisicao == 'update':
            endpoint = 'https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada
            verbo_http = 'POST'

        requisicao = self.cliente.request(endpoint, method=verbo_http)
        decodificar = requisicao[1].decode()
        return json.loads(decodificar)
