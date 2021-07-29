# Arquivo que vai importar a classe clientes.py e criar dois objetos

from clientes import Cliente
from contas import Conta

joao = Cliente("João da Silva", "7282-9298")
maria = Cliente("Maria da Cunha", "2345-8973")

conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria, joao], 2, 500)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)

conta1.extrato()
conta2.extrato()
