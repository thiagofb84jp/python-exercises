from listaUnica import *

lu = ListaUnica(int)
lu.adiciona(5)
lu.adiciona(3)
lu.adiciona(77)
lu.adiciona(18)
lu.adiciona(20)
lu.adiciona(125)

print(len(lu))

for e in lu:
    print(e)

lu.adiciona(5)

print(len(lu))

print(lu[0])

print(lu[1])
