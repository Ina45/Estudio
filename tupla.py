
import random

# Generar tres tuplas con datos aleatorios
tupla1 = (random.randint(1, 10), random.choice(["a", "b", "c"]), random.uniform(0.0, 1.0))
tupla2 = (random.randint(10, 20), random.choice(["x", "y", "z"]), random.uniform(1.0, 2.0))
tupla3 = (random.randint(100, 200), random.choice(["apple", "banana", "cherry"]), random.uniform(2.0, 3.0))

# Imprimir las tuplas generadas
print("Tupla 1:", tupla1)
print("Tupla 2:", tupla2)
print("Tupla 3:", tupla3)


import random

# Generar tres tuplas con datos aleatorios
tupla1 = (random.randint(1, 10), random.choice(["a", "b", "c"]), random.uniform(0.0, 1.0))
tupla2 = (random.randint(10, 20), random.choice(["x", "y", "z"]), random.uniform(1.0, 2.0))
tupla3 = (random.randint(100, 200), random.choice(["apple", "banana", "cherry"]), random.uniform(2.0, 3.0))

# Crear una lista que contenga las tres tuplas
lista_de_tuplas = [tupla1, tupla2, tupla3]

# Imprimir la lista de tuplas
print("Lista de Tuplas:", lista_de_tuplas)
