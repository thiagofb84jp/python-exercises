# Classe em Python

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.cor = "Cinza"


tv = Televisao()
print(tv.ligada)
print(tv.canal)
print(tv.cor)

tvSala = Televisao()
tvSala.ligada = True
tvSala.canal = 4
tvSala.cor = "Preto"

print(tv.canal)
print(tvSala.canal)
print(tvSala.cor)
