'''
Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf e idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo
'''

from cliente import Cliente
from conta import Conta

cliente = Cliente('Antonio Carlos Gomes', '111.277.148-48', 50)
conta = Conta(cliente, 250, 100)

print('Cliente')
print(cliente)

print()

print('Conta')
print(conta)

conta.sacar(10.00)
print('Saldo:', conta.consultar_saldo())

conta.depositar(40.00)
print('Saldo:', conta.consultar_saldo())

conta.sacar(10.00)
print('Saldo:', conta.consultar_saldo())

conta.sacar(150.00)
print('Saldo:', conta.consultar_saldo())

conta.sacar(200.00)
print('Saldo:', conta.consultar_saldo())

conta.sacar(30.00)
print('Saldo:', conta.consultar_saldo())

