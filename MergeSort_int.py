"""Algoritmo de Ordenamiento por Mezcla (Merge Sort) con enteros"""

import time
import json

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Cargar listas
with open('listas_enteros.json', 'r') as f:
    listas = json.load(f)
listas = {int(k): v for k, v in listas.items()}
tamaños = sorted(listas.keys())

print("Merge Sort - Enteros")
print("Tamaño\t| Tiempo(segundos)")

for n in tamaños:
    lista = listas[n].copy()
    inicio = time.process_time()
    merge_sort(lista)
    fin = time.process_time()
    print(f"{n}\t {fin - inicio:.6f}")
