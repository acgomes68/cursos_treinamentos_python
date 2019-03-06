class Conta():

    def __init__(self, cliente, saldo = 0.00, limite = 0.00):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def __str__(self):
        return 'Cliente: ' + str(self.cliente) + '\nSaldo: ' + str(self.saldo) + '\nLimite: ' + str(0 - self.limite)

    def sacar(self, valor):
        if self.saldo - valor > self.limite:
            self.saldo -= valor
            print('Valor sacado:',  valor)
        else:
            print('Erro: Saldo insuficiente!')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print('Valor depositado:', valor)
        else:
            print('Erro: Valor inválido!')

    def consultar_saldo(self):
        return self.saldo
