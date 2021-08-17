# Classe Agenda

from pythonBook.chapter10.dadoAgenda import DadoAgenda
from pythonBook.chapter10.listaUnica import ListaUnica
from pythonBook.chapter10.tipoTelefone import TipoTelefone
from pythonBook.chapter10.nome import Nome


class TiposTelefone(ListaUnica):
    def __init__(self):
        super().__init__(TipoTelefone)


class Agenda(ListaUnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tiposTelefone = TiposTelefone()

    def adicionaTipo(self, tipo):
        self.tiposTelefone.adiciona(TipoTelefone(tipo))

    def pesquisaNome(self, nome):
        if isinstance(nome, str):
            nome = Nome(nome)

        for dados in self.lista:
            if dados.nome == nome:
                return dados
            else:
                return None

    def ordena(self):
        super().ordena(lambda dado: str(dado.nome))
