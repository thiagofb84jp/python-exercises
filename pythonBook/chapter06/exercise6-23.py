"""
6.23. Controle da utilização de salas de um cinema
"""

lugaresVagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Sala (0 para sair do programa) :"))
    if sala == 0:
        print("Encerrando o programa...")
        break
    if sala > len(lugaresVagos) or sala < 1:
        print("Sala inválida!")
    elif lugaresVagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(
            input(f"Quantos lugares você deseja ({lugaresVagos[sala - 1]} \
                vagos): "))
        if lugares > lugaresVagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido.")
        else:
            lugaresVagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")

print("Utilização das salas")
for x, l in enumerate(lugaresVagos):
    print(f"Sala {x + 1} - {l} lugar(es) vazio(s)")
