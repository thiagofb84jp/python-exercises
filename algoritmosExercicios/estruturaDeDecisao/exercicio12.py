"""
12. As Organizações Tabajara resolveram dar um aumento de
        salário aos seus colaboradores e lhe contraram para
            desenvolver o programa que calculará os reajustes.
"""

salario = 1700.99

if (salario <= 280):
    salarioReajustado = ((salario / 100) * 20) + salario
    porcentagemReajuste = '20%'
    valorReajuste = (salario / 100) * 20
elif (salario > 280) and (salario <= 700):
    salarioReajustado = ((salario / 100) * 15) + salario
    porcentagemReajuste = '15%'
    valorReajuste = (salario / 100) * 15
elif (salario > 700) and (salario <= 1500):
    salarioReajustado = ((salario / 100) * 10) + salario
    porcentagemReajuste = '10%'
    valorReajuste = (salario / 100) * 10
else:
    salarioReajustado = ((salario / 100) * 5) + salario
    porcentagemReajuste = '5%'
    valorReajuste = (salario / 100) * 5

print("Salário antes do reajuste: {:.2f}".format(salario))
print("Salário reajustado: {:.2f}".format(salarioReajustado))
print("Valor do reajuste: {:.2f}".format(valorReajuste))
print("Porcentagem do reajuste: {}".format(porcentagemReajuste))
