# Desafio IF - Else

def notaConceito(valor):
    nota = float(valor)

    if (nota > 10):
        return 'Nota inválida.'
    elif (nota >= 9.1):
        return 'A'
    elif (nota >= 8.1):
        return 'A-'
