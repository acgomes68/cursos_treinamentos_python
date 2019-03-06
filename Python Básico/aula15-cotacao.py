'''
API's
- https://economia.awesomeapi.com.br/<moeda>/1
-- https://economia.awesomeapi.com.br/USD-BRL/1
-- https://economia.awesomeapi.com.br/EUR-BRL/1
-- https://economia.awesomeapi.com.br/BTC-BRL/1
- https://fixer.io/ (Somente EURO no plano gratuito)
-- http://data.fixer.io/api/latest
            ?access_key=bc4b3ede32d7b2570394c25829dab8c1
            &symbols=BRL
- https://currencylayer.com (Somente USD no plano gratuito)
-- http://www.apilayer.net/api/live
            ?access_key=c459aca9172d3cad1c42fc63b5c5e80a
            &format=1
            &currencies=BRL
'''
import requests
import json
import datetime
import time

moedas = ['USD-BRL', 'EUR-BRL', 'BTC-BRL']

while True:
    for moeda in moedas:
        requisicao = requests.get('https://economia.awesomeapi.com.br/' + moeda + '/1')
        cotacao = json.loads(requisicao.text)

        # print(cotacao)
        #[{'code': 'USD', 'ask': '3.7524', 'low': '3.7199', 'codein': 'BRL', 'create_date': '2019-02-25 17:00:01', 'pctChange': '0.01', 'bid': '3.7519', 'varBid': '0.0003', 'high': '3.7522', 'name': 'Dólar Comercial', 'timestamp': '1551129301'}]

        print('#### Cotação em {} às {} ####' . format(cotacao[0]['codein'], datetime.datetime.now()))
        print('Moeda:', cotacao[0]['code'])
        print('Valor Compra:', cotacao[0]['bid'])
        print('Valor Venda:', cotacao[0]['ask'])
        #print('Variação:', cotacao[0]['pctChange'])
        #print('Horário:', cotacao[0]['create_date'])
        print()

    time.sleep(5)
