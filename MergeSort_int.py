"""Algoritmo de Ordenamiento por Mezcla (Merge Sort) con enteros"""

import time # Para medir el tiempo de ejecución del algoritmo
import json # Para cargar las listas almacenadas en formato JSON

# Definición del algoritmo Merge Sort
def merge_sort(arr):
    """Ordena una lista de manera ascendente utilizando el algoritmo Merge Sort.
    Parámetros:
    arr (list): lista de enteros a ordenar."""
    
    if len(arr) > 1:
        # Dividir la lista en mitades
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Ordenar recursivamente cada mitad
        merge_sort(L)
        merge_sort(R)

        # Fusionar las dos mitades ordenadas
        i = j = k = 0
        # Comparar elementos de L y R y colocarlos en orden en arr
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Añadir los elementos restantes de L, si hay
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        # Añadir los elementos restantes de R, si hay
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# ------------------- Inicio del programa -------------------

# Cargar las listas de enteros desde el archivo JSON
with open('listas_enteros.json', 'r') as f:
    listas = json.load(f)
    
# Convertir las claves de string a enteros
listas = {int(k): v for k, v in listas.items()}
# Obtener los tamaños de listas en orden ascendente
tamaños = sorted(listas.keys())

# Imprimir encabezado de la tabla de resultados
print("Merge Sort - Enteros")
print("Tamaño\t| Tiempo(segundos)")

# Evaluar el tiempo de ejecución del algoritmo para cada tamaño de lista
for n in tamaños:
    lista = listas[n].copy() # Copiar la lista original para no modificarla
    inicio = time.process_time() # Marcar el tiempo antes de ordenar
    merge_sort(lista) # Ordenar la lista usando Merge Sort
    fin = time.process_time() # Marcar el tiempo después de ordenar
    print(f"{n}\t {fin - inicio:.6f}") # Imprimir tamaño y tiempo de ejecución con 6 decimales
