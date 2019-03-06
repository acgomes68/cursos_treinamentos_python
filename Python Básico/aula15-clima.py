'''
- https://openweathermap.org/api
-- http://api.openweathermap.org/data/2.5/weather
            ?q=Sao%20Paulo,br
            &units=metric
            &lang=pt
            &APPID=3e1facaadc68c97b5a90a805a3c11685
'''
import requests
import json
import goslate

cidade = input('Digite sua cidade: ')
#cidade = 'São Paulo'
requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&lang=pt&units=metric&APPID=3e1facaadc68c97b5a90a805a3c11685')
tempo = json.loads(requisicao.text)

gs = goslate.Goslate()
condicao_tempo = gs.translate(tempo['weather'][0]['main'], 'pt')

#{'base': 'stations', 'wind': {'speed': 2.1, 'deg': 220}, 'dt': 1551144900, 'id': 3448439, 'cod': 200, 'clouds': {'all': 90}, 'sys': {'message': 0.0037, 'id': 8379, 'type': 1, 'country': 'BR', 'sunset': 1551217083, 'sunrise': 1551171624}, 'visibility': 3500, 'weather': [{'description': 'moderate rain', 'main': 'Rain', 'id': 501, 'icon': '10n'}, {'description': 'mist', 'main': 'Mist', 'id': 701, 'icon': '50n'}, {'description': 'thunderstorm with heavy rain', 'main': 'Thunderstorm', 'id': 202, 'icon': '11n'}], 'coord': {'lon': -46.63, 'lat': -23.55}, 'main': {'humidity': 100, 'temp_max': 295.15, 'temp': 294.25, 'temp_min': 293.15, 'pressure': 1017}, 'name': 'São Paulo'}
print('Temperatura:', str(tempo['main']['temp']) + '\xb0C')
print('Condição do tempo:', condicao_tempo)
print('Descrição:', tempo['weather'][0]['description'])
print('Umidade:', str(tempo['main']['humidity']) + '%')
print('Mínima:', str(tempo['main']['temp_min']) + '\xb0C')
print('Máxima:', str(tempo['main']['temp_max']) + '\xb0C')
