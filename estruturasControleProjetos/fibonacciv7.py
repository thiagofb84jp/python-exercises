# Substituindo While por For

def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
        if (len(resultado) == quantidade):
            break
    return resultado


if __name__ == "__main__":
    # Listar os 20 primeiros números da sequência
    for i in fibonacci(20):
        print(i)
