# 8.36. Exemplo de tratamento de exceção com função

def ehPar(n):
    try:
        return n % 2
    except Exception:
        raise ValueError("Valor inválido.") from None
    finally:
        print("Executando antes de retornar.")


# ehPar(2)
# ehPar([])

ehPar("abc")
