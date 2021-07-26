# Exemplo de classe

class Contato:
    def __init__(self, nome, email, telefone, logradouro, cidade, estado):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.logradouro = logradouro
        self.cidade = cidade
        self.estado = estado

    def imprimeDadosEndereco(self):
        print("***** Endereço Completo *****")
        print("Nome: ", self.nome)
        print("Endereço: ", self.logradouro)
        print("Cidade: ", self.cidade)
        print("Estado: ", self.estado)


contato = Contato("Maria da Luz", "maria.luz@email.com", 992821312,
                  "Rua José dos Campos Silva, 55", "João Pessoa", "Paraíba")

contato.imprimeDadosEndereco()
