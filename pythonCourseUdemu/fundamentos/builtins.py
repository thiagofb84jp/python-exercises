# Builtins
# type() -> Doesn't work!
print(type(1))
print(__builtins__.type('Fala Galera!'))
__builtins__.print(10 / 3)
# __builtins__.help(__builtins__.dir)
print(dir())

nome = "Josefa Vianna Lima de Silva"
print(type(nome))
print(__builtins__.len(nome))
print(dir())
