'''
- Manipulação de arquivos
- Acesso a rede
- Utilização de protocolos de comunicação
- Operações com bases de dados
'''
import time

def abre_arquivo():
    try:
        open('arquivodoido.txt')
        return True
    except Exception as erro:
        print('Aconteceu algum erro: ', erro)
        return False

try:
    #dfafdsfs()
    #a = 1200 / 0
    #print('sss' + 2)
    print('Aqui todo OK agora!')
except ZeroDivisionError:
    print('Divisão por zero!')
except NameError:
    print('Função inexistente!')
except TypeError:
    print('Tipo de dado incompatível!')
except Exception as erro:
    print('Ocorreu um erro não identificado: ', erro)
    time.sleep()

print('Continuação')

i = 1
while not abre_arquivo():
    print('Tentando abrir o arquivo arquivodoido.txt...Tentativa: ', i)
    i += 1
    time.sleep(5)

print('Consegui abrir o arquivo arquivodoido.txt após {}  tentativa(s)!' . format(str(i)))