"""
5.18. Teste de Múltipla Escolha
"""

pontos = 0
questao = 1

while questao <= 3:
    resposta = input("Resposta da questão {questao}: ")
    if questao == 1 and (resposta == "b" or resposta == "B"):
        pontos += 1
    if questao == 2 and (resposta == "a" or resposta == "A"):
        pontos += 1
    if questao == 3 and (resposta == "c" or resposta == "C"):
        pontos += 1
    questao += 1

print(f"O aluno fez {pontos} pontos(s).")
