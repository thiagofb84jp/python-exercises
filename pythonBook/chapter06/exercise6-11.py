'''
6.11. Trabalhando com duas filas
'''

ultimo = 0
fila1 = []
fila2 = []

while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} \
        na fila 2.")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para \
    \a fila 2),")
    print("ou A para realizar o atendimento a fila 1 (ou B para a fila 2)")
    print("S para sair.")
    operacao = input("Operacao (F, G, A, B ou S): ")

    x = 0
    sair = False

    while x < len(operacao):
        if operacao[x] == "A" or operacao[x] == "F":
            fila = fila1
        else:
            fila = fila2
        if operacao[x] == "A" or operacao[x] == "B":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x] == "F" or operacao[x] == "G":
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        x += 1
    if sair:
        print("Encerrando programa...")
        break
