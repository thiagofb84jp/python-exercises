# Arquivo que vai importar a classe clientes.py e criar dois objetos

from clientes import Cliente
from bancos import Banco
from contas import Conta

joao = Cliente("João da Silva", "7282-9298")
maria = Cliente("Maria da Cunha", "2345-8973")
jose = Cliente("José Vargas", "7581-1923")

contaJM = Conta([joao, maria], 100101, 100.22)
contaJ = Conta([jose], 100202, 12.87)

tatu = Banco("Tatú")
tatu.abreConta(contaJM)
tatu.abreConta(contaJ)
tatu.listaContas()
