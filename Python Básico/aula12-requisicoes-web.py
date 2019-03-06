'''
- Beautiful Soup 4 BS4: pip install bs4
- PustReq: https://putsreq.com/
'''
import requests

texto = None
header = {'User-agent': 'Mac OSX',
          'Referer': 'https://google.com'}
cookie = {'ultima-visita': '10-02-2019'}
data = {'username': 'gomes',
        'password': 'gomes123'}

try:
    #requisicao = requests.get('https://putsreq.com/5topOEKpBEgL0r0apj7K')
    requisicao = requests.post('https://putsreq.com/5topOEKpBEgL0r0apj7K',
                                headers = header,
                                cookies = cookie,
                                data = data)
    if (requisicao.status_code == 200):
        texto = requisicao.text
except Exception as e:
    print('Erro na requisição: ', e)

print(texto)