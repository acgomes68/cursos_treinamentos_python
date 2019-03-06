from twitter import Twitter

consumer_key = 'ZypK3WbDKBYUfTGwGW4R7sOPN'
consumer_secret = 's0y8whYxFr03H54rwuENtt0lwzJpeLhjzu5SWpWsJWYU4bJjgQ'

token_key = '1100363977262014464-qdiSHB0awTJpBAPb0b3wze2sDjkbFi'
token_secret = 'RdB3uxpNU0U7tRQQ9MpCcbjF8KRRLHLawdDJEmEL1i8Y4'

twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)
# novo_tweet = 'NOVO teste de utilização da API através de biblioteca própria'
# objeto = twitter.tweet(novo_tweet)
# print(objeto)

query = '#palmeiras'
pesquisa = twitter.search(query)
#print(pesquisa)

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])
    print()