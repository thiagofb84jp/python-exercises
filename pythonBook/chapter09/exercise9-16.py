# 9.16. Programa para gerar arquivo paginado

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


def escreve(arquivo, linha, nLinhas, pagina):
    arquivo.write(linha + "\n")
    return verificaPagina(arquivo, nLinhas + 1, pagina)


entrada = open(NOME_DO_ARQUIVO, encoding="utf-8")
saida = open("saida_paginada.txt", "w", encoding="utf-8")

pagina = 1
linhas = 1

for linha in entrada.readlines():
    palavras = linha.rstrip().split(" ")
    linha = ""
    for p in palavras:
        p = p.strip()
        if len(linha) + len(p) + 1 > LARGURA:
            linhas, pagina = escreve(saida, linha, linhas, pagina)
            linha = " "
        linha += p + " "
    if linha != "":
        linhas, pagina = escreve(saida, linha, linhas, pagina)

while(linhas != 1):
    linhas, pagina = escreve(saida, "", linhas, pagina)


entrada.close()
saida.close()
