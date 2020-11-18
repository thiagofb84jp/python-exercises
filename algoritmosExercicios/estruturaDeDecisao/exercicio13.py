"""
13. Faça um programa para o cálculo de uma folha de pagamento,
     sabendo que os descontos são do Imposto de Renda, que depende
      do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
       e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
        (é a empresa que deposita).
"""

hora = 5.88
quantidadeHorasTrabalhadas = 220

salarioBruto = hora * quantidadeHorasTrabalhadas
fgts = (salarioBruto * 11) / 100
sindicato = (salarioBruto * 3) / 100

if (salarioBruto <= 900):
    salarioLiquido = salarioBruto - sindicato
elif (salarioBruto > 900) and (salarioBruto <= 1500):
    impostoRenda = (salarioBruto * 5) / 100
    salarioLiquido = salarioBruto - impostoRenda - sindicato
elif (salarioBruto > 1500) and (salarioBruto <= 2500):
    impostoRenda = (salarioBruto * 10) / 100
    salarioLiquido = salarioBruto - impostoRenda - sindicato
else:
    impostoRenda = (salarioBruto * 20) / 100
    salarioLiquido = salarioBruto - impostoRenda - sindicato

print("Seu salário bruto é de: {:.2f}".format(salarioBruto))
print("O valor do seu FGTS é de: {:.2f}".format(fgts))
print("O sindicato vai te levar: {:.2f}".format(sindicato))
print("Seu salário líquido é de: {:.2f}".format(salarioLiquido))
