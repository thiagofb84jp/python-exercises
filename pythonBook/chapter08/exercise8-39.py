# 8.39. Usando o random

import random

# Gerando números aleatórios com 'randit'
print("Gerando números com 'Randit'")
for x in range(10):
    print(random.randint(1, 100))
print()

# Gerando números aleatórios com 'random'
print("Gerando números com 'Random'")
for x in range(10):
    print(random.random())
print()

# Gerando números aleatórios com 'uniform'
print("Gerando números com 'Uniform'")
for x in range(10):
    print(random.uniform(15, 25))
print()

# Gerando números aleatórios com 'sample'
print("Gerando números com 'Sample'")
for x in range(10):
    print(random.sample(range(1, 101), 6))
print()

# Gerando números aleatórios com 'shuffle'
print("Gerando números com 'Shuffle'")
a = list(range(1, 11))
random.shuffle(a)
print(a)
print()

print("SJ", random.randint(10000, 99999))
print()
