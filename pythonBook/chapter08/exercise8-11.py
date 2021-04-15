# 8.10. Muda e imprime

a = 5


def mudaEImprime():
    a = 7
    print(f"'a' dentro da função {a}")


print(f"'a' antes de mudar: {a}")
mudaEImprime()
print(f"'a' depois de mudar: {a}")
