'''
https://developer.twitter.com/en/docs

Consumer API keys
ZypK3WbDKBYUfTGwGW4R7sOPN (API key)
s0y8whYxFr03H54rwuENtt0lwzJpeLhjzu5SWpWsJWYU4bJjgQ (API secret key)

Access token & access token secret
1100363977262014464-qdiSHB0awTJpBAPb0b3wze2sDjkbFi (Access token)
RdB3uxpNU0U7tRQQ9MpCcbjF8KRRLHLawdDJEmEL1i8Y4 (Access token secret)
'''
import oauth2
import json
import urllib.parse

consumer_key = 'ZypK3WbDKBYUfTGwGW4R7sOPN'
consumer_secret = 's0y8whYxFr03H54rwuENtt0lwzJpeLhjzu5SWpWsJWYU4bJjgQ'

token_key = '1100363977262014464-qdiSHB0awTJpBAPb0b3wze2sDjkbFi'
token_secret = 'RdB3uxpNU0U7tRQQ9MpCcbjF8KRRLHLawdDJEmEL1i8Y4'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key,token_secret)
cliente = oauth2.Client(consumer, token)

query = input('Novo tweet: ')
query_codificada = urllib.parse.quote(query, safe='')

requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')
decodificar = requisicao[1].decode()
objeto = json.loads(decodificar)

print(objeto)
