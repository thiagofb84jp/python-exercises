"""
5.10. Teste de Múltipla Escola
"""

pontos = 0
questao = 1

while questao <= 3:
    resposta = input("Resposta da questão {questao}: ")
    if questao == 1 and resposta == "b":
        pontos += 1
    if questao == 2 and resposta == "a":
        pontos += 1
    if questao == 3 and resposta == "d":
        pontos += 1
    questao += 1

print(f"O aluno fez {pontos} pontos(s).")
