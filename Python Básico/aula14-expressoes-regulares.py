'''
RAW String: interpreta caracteres especiais como string.
Ex.:
print('Primeira linha\nSegunda Linha')
Primeira linha
Segunda Linha

print(r'Primeira linha\nSegunda Linha')
Primeira linha\nSegunda Linha
'''
import re
import requests

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
indice = iter(myclass)

print('teste ', str(next(indice)))
teste = 'O gato é bonito'
padrao = re.search(r'gat.', teste)
if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
teste = 'O gat é bonito'
padrao = re.search(r'gat\w', teste)
if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
teste = 'O gat é bonito'
padrao = re.search(r'\w\w\w\w', teste)
if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
teste = 'O gato, a gata, os gatinhos e os gatões'
padrao = re.findall(r'gat\w', teste)
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
teste = 'Um gat, o gato, a gata, os gatinhos e os gatões'
padrao = re.findall(r'gat\w+', teste)
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
teste = 'Um gat, o gato, a gata, os gatinhos e os gatões'
padrao = re.findall(r'gat\w*', teste)
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
teste = 'Um gat, o gato, a gata, os gatinhos e os gatões'
padrao = re.findall(r'[gat]', teste)
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
teste = 'Um gat, o gato, a gata, os gatinhos e os gatões'
padrao = re.findall(r'[gat]+', teste)
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
teste = 'Um gat, o gato, a gata, os gatinhos e os gatões'
padrao = re.findall(r'\w{4,6}', teste)
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
lista_testes = ['acgomes68@gmail.com', 'antonio.gomes@3ptecnologia.com']
for teste in lista_testes:
    padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', teste)
    if padrao:
        print(padrao)
    else:
        print('Padrão não encontrado')
print()

print('teste ', str(next(indice)))
requisicao = requests.get('https://corretora.miraeasset.com.br/Home/Perguntas')

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')
print()