# 8.23. Função com passagem de parâmetros obrigatórios

# Função retângulo com parâmetros obrigatórios e opcionais
def retangulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)

    print()


retangulo(3, 4)
retangulo(largura=3, altura=4)
retangulo(altura=3, largura=4)
retangulo(caractere="-", altura=4, largura=3)
