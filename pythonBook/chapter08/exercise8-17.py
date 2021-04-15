# Calculando, de forma recursiva, o MDC

def mdc(a, b):
    if b == 0:
        return a

    return mdc(b, a % b)


def mmc(a, b):
    return abs(a * b) / mdc(a, b)


print(f"MMC 10 e 5 --> {mdc(10, 5)}")
print(f"MMC 32 e 24 --> {mdc(32, 24)}")
print(f"MMC 5 e 3 --> {mdc(5, 3)}")
