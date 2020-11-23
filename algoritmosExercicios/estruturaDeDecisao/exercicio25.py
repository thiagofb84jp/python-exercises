"""
25. Faça um programa que faça 5 perguntas
    para uma pessoa sobre um crime.
"""


def gerarPerguntas():

    quantidadePositivo = 0

    status = {
        2: "Suspeito(a)",
        3: "Cúmplice",
        4: "Cúmplice",
        5: "Assassino"
    }

    listaPerguntas = ["Telefonou para a vítima?", "Esteve no local do crime?",
                      "Mora perto da vítima?", "Devia para a vítima?",
                      "Já trabalhou com a vítima?"]

    for index in len(listaPerguntas):
        print(listaPerguntas[index] + " ( sim ou não ).")

    resposta = "Sim"

    if (resposta.lower() == 'sim'):
        quantidadePositivo += 1

    if (quantidadePositivo in status):
        print(status[quantidadePositivo])
    else:
        print("Inocente")
