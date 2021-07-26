# Associando um comportamento à classe Televisao()

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def mudaCanalParaBaixo(self):
        self.canal -= 1

    def mudaCanalParaCima(self):
        self.canal += 1


tv = Televisao()
tv.mudaCanalParaCima()
tv.mudaCanalParaCima()
print(tv.canal)

tv.mudaCanalParaBaixo()
print(tv.canal)