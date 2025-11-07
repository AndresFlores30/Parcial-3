def quicksort(arr):
    """
    Ordenamiento QuickSort recursivo
    """
    if len(arr) <= 1:
        return arr
    
    # Elegir pivote (en este caso, el elemento del medio)
    pivote = arr[len(arr) // 2]
    
    # Dividir en tres listas
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    
    # Ordenar recursivamente y combinar
    return quicksort(izquierda) + medio + quicksort(derecha)

def quicksort_detallado(arr, nivel=0):
    """
    Version que muestra el proceso paso a paso
    """
    if len(arr) <= 1:
        print("  " * nivel + f"Caso base: {arr}")
        return arr
    
    pivote = arr[len(arr) // 2]
    print("  " * nivel + f"Array: {arr}")
    print("  " * nivel + f"Pivote: {pivote}")
    
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    
    print("  " * nivel + f"Izquierda: {izquierda}")
    print("  " * nivel + f"Medio: {medio}")
    print("  " * nivel + f"Derecha: {derecha}")
    print("  " * nivel + "---")
    
    resultado = quicksort_detallado(izquierda, nivel + 1) + medio + quicksort_detallado(derecha, nivel + 1)
    print("  " * nivel + f"Combinado: {resultado}")
    
    return resultado

def mostrar_proceso_rapido(arr):
    """
    Muestra el proceso de forma mas compacta
    """
    print("PROCESO DE QUICKSORT")
    print("===================")
    print(f"Array original: {arr}")
    print()
    
    resultado = quicksort_detallado(arr)
    print(f"\nArray ordenado: {resultado}")
    return resultado

def prueba_quicksort():
    """
    Pruebas basicas del algoritmo
    """
    print("PRUEBAS DE QUICKSORT")
    print("===================")
    
    pruebas = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3],
        []
    ]
    
    for i, arr in enumerate(pruebas, 1):
        print(f"\nPrueba {i}: {arr}")
        resultado = quicksort(arr)
        print(f"Ordenado: {resultado}")

def ejemplo_simple():
    """
    Ejemplo muy simple para entender
    """
    print("EJEMPLO SIMPLE")
    print("==============")
    
    numeros = [5, 2, 8, 1, 9]
    print(f"Array: {numeros}")
    
    # Primera division
    pivote = numeros[2]  # 8
    print(f"Pivote: {pivote}")
    
    izquierda = [x for x in numeros if x < pivote]  # [5, 2, 1]
    medio = [x for x in numeros if x == pivote]     # [8]
    derecha = [x for x in numeros if x > pivote]    # [9]
    
    print(f"Izquierda: {izquierda}")
    print(f"Medio: {medio}")
    print(f"Derecha: {derecha}")
    
    # Ordenar izquierda
    print("\nOrdenando izquierda:")
    if izquierda:
        pivote_izq = izquierda[len(izquierda) // 2]  # 2
        print(f"Pivote izquierda: {pivote_izq}")
        izq_izq = [x for x in izquierda if x < pivote_izq]  # [1]
        izq_med = [x for x in izquierda if x == pivote_izq] # [2]
        izq_der = [x for x in izquierda if x > pivote_izq]  # [5]
        izquierda_ordenada = izq_izq + izq_med + izq_der
        print(f"Izquierda ordenada: {izquierda_ordenada}")
    else:
        izquierda_ordenada = []
    
    resultado_final = izquierda_ordenada + medio + derecha
    print(f"\nResultado final: {resultado_final}")

def comparar_con_python():
    """
    Compara con la funcion sorted de Python
    """
    print("\nCOMPARACION CON PYTHON")
    print("=====================")
    
    arr = [30, 10, 50, 20, 40, 60]
    print(f"Array: {arr}")
    
    quick_result = quicksort(arr)
    python_result = sorted(arr)
    
    print(f"QuickSort: {quick_result}")
    print(f"Python: {python_result}")
    print(f"Son iguales: {quick_result == python_result}")

def explicar_quicksort():
    """
    Explica como funciona el algoritmo
    """
    print("\nCOMO FUNCIONA QUICKSORT")
    print("======================")
    print("1. Elegir un elemento como pivote")
    print("2. Dividir el array en tres partes:")
    print("   - Elementos menores que el pivote")
    print("   - Elementos iguales al pivote")
    print("   - Elementos mayores que el pivote")
    print("3. Ordenar recursivamente las partes izquierda y derecha")
    print("4. Combinar: izquierda + medio + derecha")
    print("5. Caso base: arrays de 0 o 1 elemento ya estan ordenados")

# Programa principal
if __name__ == "__main__":
    # Ejemplo principal
    print("EJEMPLO PRINCIPAL")
    print("================")
    arr_principal = [50, 30, 70, 20, 40, 60, 80]
    mostrar_proceso_rapido(arr_principal)
    
    # Pruebas basicas
    prueba_quicksort()
    
    # Ejemplo simple
    ejemplo_simple()
    
    # Comparacion
    comparar_con_python()
    
    # Explicacion
    explicar_quicksort()
    
    # Ejemplo final
    print("\nEJEMPLO FINAL - VERSION SIMPLE")
    print("==============================")
    arr_final = [64, 34, 25, 12, 22]
    print(f"Array: {arr_final}")
    resultado_final = quicksort(arr_final)
    print(f"Ordenado: {resultado_final}")