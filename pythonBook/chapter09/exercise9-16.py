# 9.16.

LARGURA = 76
LINHAS = 60
NOME_DO_ARQUIVO = "mobydick.txt"


def verificaPagina(arquivo, linha, pagina):
    if linha == LINHAS:
        rodape = f"= {NOME_DO_ARQUIVO} - Página: {pagina} ="
        arquivo.write(rodape.center(LARGURA - 1) + "\n")
        pagina += 1
        linha = 1
    return linha, pagina


"""
Continuar o exercício na criação da função def escreve(arquivo, linha, nLinhas, pagina):
https://python.nilo.pro.br/exercicios3/capitulo%2009/exercicio-9-7.html
"""
