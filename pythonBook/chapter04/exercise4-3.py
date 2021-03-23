"""
4.3. Calcula velocidade do carro
"""

velocidade = int(input("Digite a velocidade do seu carro: "))

if (velocidade <= 80):
    print("Sua velocidade está OK, boa viagem!")
else:
    multa = (velocidade - 80) * 5
    print("Velocidade acima de 80 Km/h.")
    print(f"Você foi multado em R$ {multa}.")
