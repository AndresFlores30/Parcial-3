def bubble_sort(arr):
    """
    Ordenamiento por Intercambio (Bubble Sort)
    Complejidad: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        # Bandera para optimizacion
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Si no hubo intercambios, el array esta ordenado
        if not swapped:
            break
    return arr

def bubble_sort_desc(arr):
    """
    Ordenamiento por Intercambio en orden descendente
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def mostrar_proceso(arr):
    """
    Muestra el proceso paso a paso del ordenamiento
    """
    print("Array original:", arr)
    n = len(arr)
    
    for i in range(n):
        print(f"\nPasada {i + 1}:")
        swapped = False
        
        for j in range(0, n - i - 1):
            print(f"  Comparando {arr[j]} y {arr[j + 1]}", end="")
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(" -> INTERCAMBIO")
            else:
                print(" -> no intercambia")
            
            print(f"  Array actual: {arr}")
        
        if not swapped:
            print("  No hubo intercambios - array ordenado")
            break
    
    print(f"\nArray final ordenado: {arr}")
    return arr

def prueba_bubble_sort():
    """
    Pruebas basicas del metodo de intercambio
    """
    print("PRUEBAS DEL METODO DE ORDENAMIENTO POR INTERCAMBIO")
    print("==============================================")
    
    # Casos de prueba
    pruebas = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5],
        [42],
        []
    ]
    
    for i, arr in enumerate(pruebas, 1):
        print(f"\nPrueba {i}:")
        print(f"Entrada:  {arr}")
        
        resultado = bubble_sort(arr.copy())
        esperado = sorted(arr)
        
        print(f"Salida:   {resultado}")
        print(f"Esperado: {esperado}")
        print(f"Correcto: {resultado == esperado}")

def comparar_versiones():
    """
    Compara la version normal con la descendente
    """
    print("\nCOMPARACION DE VERSIONES")
    print("========================")
    
    arr = [64, 34, 25, 12, 90]
    print(f"Array original: {arr}")
    
    ascendente = bubble_sort(arr.copy())
    descendente = bubble_sort_desc(arr.copy())
    
    print(f"Ascendente:  {ascendente}")
    print(f"Descendente: {descendente}")

def ejemplo_simple():
    """
    Ejemplo simple y claro del metodo
    """
    print("\nEJEMPLO SIMPLE")
    print("==============")
    
    # Ejemplo con numeros pequenos
    numeros = [5, 2, 8, 1, 9]
    print("Array inicial:", numeros)
    
    # Primera pasada
    print("\nPrimera pasada:")
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            print(f"Intercambiar {numeros[j]} y {numeros[j + 1]}")
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
        print(f"Estado: {numeros}")
    
    print("\nArray despues de primera pasada:", numeros)

def rendimiento_bubble():
    """
    Muestra el rendimiento con diferentes tamanos
    """
    import time
    import random
    
    print("\nPRUEBA DE RENDIMIENTO")
    print("====================")
    
    tamanos = [100, 500, 1000]
    
    for tamano in tamanos:
        # Generar array aleatorio
        arr = [random.randint(1, 1000) for _ in range(tamano)]
        
        # Medir tiempo
        inicio = time.time()
        bubble_sort(arr.copy())
        fin = time.time()
        
        tiempo = fin - inicio
        print(f"Tamano {tamano}: {tiempo:.4f} segundos")

# Programa principal
if __name__ == "__main__":
    # Pruebas basicas
    prueba_bubble_sort()
    
    # Comparacion de versiones
    comparar_versiones()
    
    # Ejemplo simple
    ejemplo_simple()
    
    # Demostracion detallada
    print("\nDEMOSTRACION DETALLADA")
    print("=====================")
    arr_demo = [29, 10, 14, 37, 13]
    mostrar_proceso(arr_demo.copy())
    
    # Prueba de rendimiento
    rendimiento_bubble()
    
    # Ejemplo final
    print("\nEJEMPLO FINAL")
    print("=============")
    arr_final = [64, 34, 25, 12, 22, 11, 90]
    print("Array original:", arr_final)
    resultado_final = bubble_sort(arr_final.copy())
    print("Array ordenado:", resultado_final)