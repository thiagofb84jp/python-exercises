"""
4.14. Calcula empréstimo casa
"""

valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário: "))
anos = int(input("Quantos anos para pagar: "))

meses = anos * 12
prestacao = valor / meses

if prestacao > salario * 0.3:
    print("Infelizmente você  não pode obter o empréstimo.")
else:
    print(f"Valor da prestação: R$ {prestacao:7.2f} Empréstimo OK")
