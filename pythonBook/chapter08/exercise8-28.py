# Valida a entrada de uma função


def validaEntrada(mensagem, opcoesValidas):
    opcoes = opcoesValidas.lower()

    while True:
        escolha = input(mensagem)
        if escolha.lower() in opcoes:
            break
        print("Erro: opção inválida. Redigite.\n")

    return escolha


validaEntrada("Escolha uma opção: ", "abcde")
