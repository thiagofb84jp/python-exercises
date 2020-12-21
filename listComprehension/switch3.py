# Simulando Switch #03

def getTipoDia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana',
    }
    diaEscolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(diaEscolhido, '** dia inválido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {getTipoDia(dia)}')
