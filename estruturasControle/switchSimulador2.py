# Simulador do Switch - Parte 2

def getTipoDia(dia):
    dias = {
        1: 'Fim de Semana',
        2: 'Dia de Semana',
        3: 'Dia de Semana',
        4: 'Dia de Semana',
        5: 'Dia de Semana',
        6: 'Dia de Semana',
        7: 'Fim de Semana',
    }
    return dias.get(dia, '** dia inválido **')


if __name__ == "__main__":
    for dia in range(8):
        print(f'{dia}: {getTipoDia(dia)}')
