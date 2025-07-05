"""Genera y guarda listas de enteros y decimales para pruebas de algoritmos"""

import random
import json

random.seed(42)
tamaños = [15000, 25000, 30000, 35000, 40000, 45000]

# Listas de enteros
listas_enteros = {str(n): [random.randint(0, 100000) for _ in range(n)] for n in tamaños}

# Listas de decimales
random.seed(42)
listas_decimales = {str(n): [random.uniform(0, 100000) for _ in range(n)] for n in tamaños}

# Guardar archivos
with open('listas_enteros.json', 'w') as f:
    json.dump(listas_enteros, f)

with open('listas_decimales.json', 'w') as f:
    json.dump(listas_decimales, f)

print("Listas guardadas como 'listas_enteros.json' y 'listas_decimales.json'")
