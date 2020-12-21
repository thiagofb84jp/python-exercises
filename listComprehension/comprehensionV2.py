# List Comprehension #02

# [ expressao for item in list if condicional ]
dobroDosPares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobroDosPares)

# versão normal
dobroDosPares = []
for i in range(10):
    if (i % 2 == 0):
        dobroDosPares.append(i * 2)

print(dobroDosPares)
