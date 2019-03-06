def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

def imprime_oi():
    print('oi')

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

retorno = soma(75, 1289)
print(retorno)

retorno = round(soma(12.54, 14.87), 2)
print(retorno)

imprime_oi()

print(tem_sete_itens('oi pessoal'))

if tem_sete_itens('1234567'):
    print('realmente tem 7 números')

if tem_sete_itens({1,2,3,4,5,6,7}):
    print('realmente tem 7 itens')

if tem_sete_itens({1,2,3,4,5,6,7,8}):
    print('realmente tem 7 itens')