"""Algoritmo de Ordenamiento por Selección (Selection Sort) con enteros"""

import time
import json

# Cargar listas
with open('listas_enteros.json', 'r') as f:
    listas = json.load(f)
listas = {int(k): v for k, v in listas.items()}
tamaños = sorted(listas.keys())

print("Selection Sort - Enteros")
print("Tamaño\t| Tiempo(segundos)")

for n in tamaños:
    lista = listas[n].copy()
    inicio = time.process_time()

    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

    fin = time.process_time()
    print(f"{n}\t {fin - inicio:.6f}")
