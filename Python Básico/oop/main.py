from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 8, 'Ford', 10)

print('CAMINHÃO ROSA')
print(caminhao_rosa)
print(type(caminhao_rosa))
print('Cor:' , caminhao_rosa.cor)
print('Rodas:', caminhao_rosa.rodas)
print('Marca:', caminhao_rosa.marca)
print('Tanque:', caminhao_rosa.tanque)

print()

print('CARRO ZUL')
carro_azul = Carro('azul', 'BMW', 30)
print(carro_azul)
print(type(carro_azul))
print('Cor:' , carro_azul.cor)
print('Rodas:', carro_azul.rodas)
print('Marca:', carro_azul.marca)
print('Tanque:', carro_azul.tanque)

carro_azul.abastecer(20)
print('Tanque:', carro_azul.tanque)

carro_azul.abastecer(10)
print('Tanque:', carro_azul.tanque)