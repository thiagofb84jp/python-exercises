# 9.11. Controle de uma agenda de telefones

agenda = []


def pedeNome():
    return input("Nome: ")


def pedeTelefone():
    return input("Telefone: ")


def mostraDados(nome, telefone):
    print(f"Nome: {nome} | Telefone: {telefone}")


def pedeNomeArquivo():
    return input("Nome do arquivo: ")


def pesquisa(nome):
    mNome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mNome:
            return p
    return None


def novo():
    global agenda
    nome = pedeNome()
    telefone = pedeTelefone()
    agenda.append([nome, telefone])


def apaga():
    global agenda
    nome = pedeNome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print("Nome não encontrado.")


def altera():
    p = pesquisa(pedeNome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado: ")
        mostraDados(nome, telefone)
        nome = pedeNome()
        telefone = pedeTelefone()
        agenda[p] = [nome, telefone]
    else:
        print("Nome não encontrado.")


def lista():
    print("\nAgenda\n\n------")
    for e in agenda:
        mostraDados(e[0], e[1])
    print("------\n")


def le():
    global agenda
    nomeArquivo = pedeNomeArquivo()
    with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for lines in arquivo.readlines():
            nome, telefone = lines.strip().split("#")
            agenda.append([nome, telefone])


def grava():
    nomeArquivo = pedeNomeArquivo()
    with open(nomeArquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")


def validaFaixaInteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

"""
>> CONTINUAR A CODIFICAÇÃO DA PÁGINA 204
"""
