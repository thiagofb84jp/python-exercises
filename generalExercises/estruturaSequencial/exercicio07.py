# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o lado do quadrado (em metros): "))

area = lado * lado

print("Área do quadrado: {:.2f}".format(area))
print("Dobro da área do quadrado {:.2f} em metros quadrados.".format(area * 2))
