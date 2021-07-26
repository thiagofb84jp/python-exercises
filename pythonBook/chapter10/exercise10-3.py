# Passagem de parâmetros dentro de uma classe

class Televisao:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = 2
        self.cMin = min
        self.cMax = max

    def mudaCanalParaBaixo(self):
        if self.canal - 1 >= self.cMin:
            self.canal -= 1

    def mudaCanalParaCima(self):
        if self.canal + 1 <= self.cMax:
            self.canal += 1


tv = Televisao(1, 99)

for x in range(0, 120):
    tv.mudaCanalParaCima()

print(tv.canal)

for x in range(0, 120):
    tv.mudaCanalParaBaixo()
    
print(tv.canal)
