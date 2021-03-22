"""
3.15. Calcular expectativa de vida do fumante.
"""

cigarrosPorDia = int(input("Digite a quantidade de cigarros por dia: "))
anosFumando = float(input("Quantidade de anos fumando: "))
reducaoEmMinutos = anosFumando * 365 * cigarrosPorDia * 10

reducaoEmDias = reducaoEmMinutos / (24 * 60)

print(f"Redução do tempo de vida em {reducaoEmDias:.0f} dias.")
