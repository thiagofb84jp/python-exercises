# Função que retorna o múltiplo de um número

def multiplo(a, b):
    return a % b == 0


print(f"múltiplo(8, 4) == True -> obtido: {multiplo(8, 4)}")
print(f"múltiplo(7, 3) == False -> obtido: {multiplo(7, 3)}")
print(f"múltiplo(5, 5) == True -> obtido: {multiplo(5, 5)}")
