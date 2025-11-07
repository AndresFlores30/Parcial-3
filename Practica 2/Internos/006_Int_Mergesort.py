def mergesort(arr):
    """
    Ordenamiento MergeSort recursivo
    """
    if len(arr) <= 1:
        return arr
    
    # Dividir el array en dos mitades
    medio = len(arr) // 2
    izquierda = arr[:medio]
    derecha = arr[medio:]
    
    # Ordenar recursivamente
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    
    # Combinar las mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    """
    Combina dos arrays ordenados en uno solo ordenado
    """
    resultado = []
    i = j = 0
    
    # Comparar elementos y agregar el menor
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agregar elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

def mergesort_detallado(arr, nivel=0):
    """
    Version que muestra el proceso paso a paso
    """
    espacios = "  " * nivel
    print(f"{espacios}Dividiendo: {arr}")
    
    if len(arr) <= 1:
        print(f"{espacios}Caso base: {arr}")
        return arr
    
    medio = len(arr) // 2
    izquierda = arr[:medio]
    derecha = arr[medio:]
    
    print(f"{espacios}Izquierda: {izquierda}, Derecha: {derecha}")
    
    izquierda_ordenada = mergesort_detallado(izquierda, nivel + 1)
    derecha_ordenada = mergesort_detallado(derecha, nivel + 1)
    
    resultado = merge(izquierda_ordenada, derecha_ordenada)
    print(f"{espacios}Combinando: {izquierda_ordenada} + {derecha_ordenada} = {resultado}")
    
    return resultado

def mostrar_proceso(arr):
    """
    Muestra el proceso completo de MergeSort
    """
    print("PROCESO DE MERGESORT")
    print("===================")
    print(f"Array original: {arr}")
    print()
    
    resultado = mergesort_detallado(arr)
    print(f"\nArray ordenado: {resultado}")
    return resultado

def prueba_mergesort():
    """
    Pruebas basicas del algoritmo
    """
    print("PRUEBAS DE MERGESORT")
    print("===================")
    
    pruebas = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5],
        [42],
        []
    ]
    
    for i, arr in enumerate(pruebas, 1):
        print(f"\nPrueba {i}: {arr}")
        resultado = mergesort(arr)
        print(f"Ordenado: {resultado}")

def ejemplo_merge():
    """
    Ejemplo de como funciona la funcion merge
    """
    print("EJEMPLO DE COMBINACION (MERGE)")
    print("==============================")
    
    izquierda = [2, 5, 8]
    derecha = [1, 3, 6]
    print(f"Izquierda ordenada: {izquierda}")
    print(f"Derecha ordenada: {derecha}")
    
    resultado = merge(izquierda, derecha)
    print(f"Combinado: {resultado}")
    
    print("\nProceso de combinacion:")
    i = j = 0
    izquierda = [2, 5, 8]
    derecha = [1, 3, 6]
    resultado = []
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            print(f"  Agregar {izquierda[i]} de izquierda")
            i += 1
        else:
            resultado.append(derecha[j])
            print(f"  Agregar {derecha[j]} de derecha")
            j += 1
    
    # Agregar restantes
    if i < len(izquierda):
        print(f"  Agregar resto de izquierda: {izquierda[i:]}")
        resultado.extend(izquierda[i:])
    if j < len(derecha):
        print(f"  Agregar resto de derecha: {derecha[j:]}")
        resultado.extend(derecha[j:])
    
    print(f"Resultado final: {resultado}")

def comparar_con_python():
    """
    Compara con la funcion sorted de Python
    """
    print("\nCOMPARACION CON PYTHON")
    print("=====================")
    
    arr = [30, 10, 50, 20, 40, 60]
    print(f"Array: {arr}")
    
    merge_result = mergesort(arr)
    python_result = sorted(arr)
    
    print(f"MergeSort: {merge_result}")
    print(f"Python: {python_result}")
    print(f"Son iguales: {merge_result == python_result}")

def explicar_mergesort():
    """
    Explica como funciona el algoritmo
    """
    print("\nCOMO FUNCIONA MERGESORT")
    print("======================")
    print("1. DIVIDIR:")
    print("   - Dividir el array en dos mitades iguales")
    print("   - Repetir hasta tener arrays de 0 o 1 elemento")
    print("2. CONQUISTAR:")
    print("   - Arrays de 0 o 1 elemento ya estan ordenados")
    print("3. COMBINAR:")
    print("   - Combinar dos arrays ordenados en uno ordenado")
    print("   - Comparar primeros elementos y tomar el menor")
    print("4. Complejidad: O(n log n) en todos los casos")

# Programa principal
if __name__ == "__main__":
    # Ejemplo principal
    print("EJEMPLO PRINCIPAL")
    print("================")
    arr_principal = [38, 27, 43, 3, 9, 82, 10]
    mostrar_proceso(arr_principal)
    
    # Ejemplo de combinacion
    ejemplo_merge()
    
    # Pruebas basicas
    prueba_mergesort()
    
    # Comparacion
    comparar_con_python()
    
    # Explicacion
    explicar_mergesort()
    
    # Ejemplo final simple
    print("\nEJEMPLO FINAL - VERSION SIMPLE")
    print("==============================")
    arr_final = [64, 34, 25, 12]
    print(f"Array: {arr_final}")
    resultado_final = mergesort(arr_final)
    print(f"Ordenado: {resultado_final}")