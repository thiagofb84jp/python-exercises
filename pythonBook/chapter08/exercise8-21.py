# 8.21. Validação de inteiro usando função
def faixaInt(pergunta, minimo, maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print(f"Valor inválido. Digite um valor entre {minimo} e {maximo}")
        else:
            return v


faixaInt("Digite um valor entre 0 e 7: ", 0, 7)
