'''
5.19. Calcula poupança (1)
'''

deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))

mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * taxa / 100)
    print(f"Saldo do mês {mes} é de R${saldo:5.2f}")
    mes += 1

print("O ganho obtido com os juros foi de R${saldo - deposito:8.2f}.")
