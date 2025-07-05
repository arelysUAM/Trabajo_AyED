"""Algoritmo de Ordenamiento Rápido (Quick Sort) con enteros"""

import time
import json

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x < pivote]
        iguales = [x for x in arr if x == pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quick_sort(menores) + iguales + quick_sort(mayores)

# Cargar listas
with open('listas_enteros.json', 'r') as f:
    listas = json.load(f)
listas = {int(k): v for k, v in listas.items()}
tamaños = sorted(listas.keys())

print("Quick Sort - Enteros")
print("Tamaño\t| Tiempo(segundos)")

for n in tamaños:
    lista = listas[n].copy()
    inicio = time.process_time()
    lista = quick_sort(lista)
    fin = time.process_time()
    print(f"{n}\t {fin - inicio:.6f}")
