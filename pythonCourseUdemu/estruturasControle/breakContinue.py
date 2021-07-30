# Break - Continue

# Continue - Quando acha a premissa, continua no laço
for x in range(1, 11):
    if ((x % 2) == 0):
        continue
    print(x)

print()

# Break - Sai do laço de iteração
for x in range(1, 11):
    if (x == 5):
        break
    print(x)

print("Fim!")
