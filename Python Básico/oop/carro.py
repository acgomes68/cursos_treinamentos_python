from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        rodas = 4
        Veiculo.__init__(self, cor, rodas, marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print('Erro: tanque cheio!')
        else:
            self.tanque += litros