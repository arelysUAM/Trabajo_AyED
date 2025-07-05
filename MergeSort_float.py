"""Algoritmo de Ordenamiento por Mezcla (Merge Sort) con decimales"""

import time # Para medir el tiempo de ejecución
import json # Para cargar las listas almacenadas en formato JSON

# Definición del algoritmo Merge Sort
def merge_sort(arr):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo Merge Sort.
    
    Parámetros:
    arr (list): lista de números decimales a ordenar.
    """
    if len(arr) > 1:
        # Dividir la lista en mitades
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Aplicar recursivamente el algoritmo en cada mitad
        merge_sort(L)
        merge_sort(R)

        # Fusionar ambas mitades ordenadas
        i = j = k = 0
        # Comparar elementos de ambas mitades y ordenar en la lista original
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        # Agregar los elementos restantes de la mitad izquierda
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        # Agregar los elementos restantes de la mitad derecha
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
# ------------------- Inicio del programa -------------------

# Cargar las listas de decimales desde el archivo JSON
with open('listas_decimales.json', 'r') as f:
    listas = json.load(f)
# Convertir las claves (originalmente cadenas) a enteros
listas = {int(k): v for k, v in listas.items()}
# Obtener la lista de tamaños ordenada
tamaños = sorted(listas.keys())

# Imprimir encabezado de resultados
print("Merge Sort - Decimales")
print("Tamaño\t| Tiempo(segundos)")

# Ejecutar el algoritmo para cada tamaño de lista y medir su tiempo
for n in tamaños:
    lista = listas[n].copy() # Copiar la lista para no modificar el original
    inicio = time.process_time() # Medir tiempo antes de ordenar
    merge_sort(lista) # Ordenar la lista
    fin = time.process_time() # Medir tiempo después de ordenar
    print(f"{n}\t {fin - inicio:.6f}") # Mostrar resultados con precisión de 6 decimales
