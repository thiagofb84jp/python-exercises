# Classe Menu (menu principal do programa Agenda)

class Menu:
    def __init__(self):
        self.opcoes = [["Sair", None]]

    def adicionaOpcoes(self, nome, funcao):
        self.opcoes.append([nome, funcao])

    def exibe(self):
        print("=====")
        print("Menu")
        print("=====\n")

        for i, opcao in enumerate(self.opcoes):
            print(f"[{i}] - {opcao[0]}")
        print()

    def execute(self):
        while True:
            self.exibe()
            escolha = validaFaixaInteiro("Escolha uma opção: ",
                                         0, len(self.opcoes) - 1)
            if escolha == 0:
                break
            self.opcoes[escolha][1]()
