def selection_sort(arr):
    """
    Ordenamiento por Selección
    Complejidad: O(n²) en todos los casos
    """
    n = len(arr)
    for i in range(n):
        # Encontrar el mínimo en el resto del array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar el mínimo con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def selection_sort_desc(arr):
    """
    Ordenamiento por Selección en orden descendente
    """
    n = len(arr)
    for i in range(n):
        # Encontrar el máximo en el resto del array
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        # Intercambiar el máximo con el primer elemento no ordenado
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def selection_sort_verbose(arr):
    """
    Versión detallada que muestra cada paso
    """
    n = len(arr)
    print(f"Array inicial: {arr}")
    
    for i in range(n):
        print(f"\n--- Iteración {i + 1} ---")
        print(f"Subarray no ordenado: {arr[i:]}")
        
        min_idx = i
        print(f"Elemento actual en posición {i}: {arr[i]}")
        
        # Buscar el mínimo
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"  Nuevo mínimo encontrado: {arr[j]} en posición {j}")
        
        if min_idx != i:
            print(f"Intercambiando {arr[i]} (posición {i}) con {arr[min_idx]} (posición {min_idx})")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"El elemento {arr[i]} ya está en la posición correcta")
        
        print(f"Array después de iteración {i + 1}: {arr}")
    
    return arr

def test_selection_sort():
    """
    Función completa de pruebas para el método de selección
    """
    print("PRUEBAS DEL MÉTODO DE ORDENAMIENTO POR SELECCIÓN")
    print("=" * 65)
    
    # Casos de prueba
    test_cases = [
        {
            "name": "Caso básico desordenado",
            "input": [64, 34, 25, 12, 22, 11, 90],
            "expected": [11, 12, 22, 25, 34, 64, 90]
        },
        {
            "name": "Array pequeño",
            "input": [5, 2, 4, 6, 1, 3],
            "expected": [1, 2, 3, 4, 5, 6]
        },
        {
            "name": "Array ya ordenado",
            "input": [1, 2, 3, 4, 5],
            "expected": [1, 2, 3, 4, 5]
        },
        {
            "name": "Array ordenado inverso",
            "input": [5, 4, 3, 2, 1],
            "expected": [1, 2, 3, 4, 5]
        },
        {
            "name": "Array con duplicados",
            "input": [3, 1, 4, 1, 5, 9, 2, 6, 5],
            "expected": [1, 1, 2, 3, 4, 5, 5, 6, 9]
        },
        {
            "name": "Array con un elemento",
            "input": [42],
            "expected": [42]
        },
        {
            "name": "Array vacío",
            "input": [],
            "expected": []
        },
        {
            "name": "Array con elementos iguales",
            "input": [7, 7, 7, 7, 7],
            "expected": [7, 7, 7, 7, 7]
        },
        {
            "name": "Array con números negativos",
            "input": [5, -2, 0, -8, 3],
            "expected": [-8, -2, 0, 3, 5]
        },
        {
            "name": "Array con números grandes",
            "input": [1000, 1, 100, 10],
            "expected": [1, 10, 100, 1000]
        }
    ]
    
    # Ejecutar pruebas
    passed_tests = 0
    total_tests = len(test_cases)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n Test {i}: {test['name']}")
        print(f"   Input:    {test['input']}")
        
        # Hacer copia para no modificar el original
        input_copy = test['input'].copy()
        result = selection_sort(input_copy)
        
        print(f"   Expected: {test['expected']}")
        print(f"   Result:   {result}")
        
        # Verificar resultado
        if result == test['expected']:
            print("    PASSED")
            passed_tests += 1
        else:
            print(" FAILED")
    
    # Mostrar resumen
    print("\n" + "=" * 65)
    print(f" RESUMEN DE PRUEBAS: {passed_tests}/{total_tests} correctos")
    print(f" Porcentaje de éxito: { (passed_tests/total_tests)*100:.1f}%")

def visual_selection_sort_demo():
    """
    Demostración visual paso a paso del algoritmo
    """
    print("\n🎬 DEMOSTRACIÓN VISUAL PASO A PASO")
    print("=" * 55)
    
    arr = [64, 25, 12, 22, 11]
    print(f"Array original: {arr}")
    print("\nProceso de ordenamiento:")
    
    n = len(arr)
    for i in range(n):
        print(f"\n--- Iteración {i + 1} ---")
        print(f"Buscando mínimo en: {arr[i:]}")
        
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"  Nuevo mínimo: {arr[j]} en posición {j}")
        
        if min_idx != i:
            print(f"Intercambiando {arr[i]} (pos {i}) con {arr[min_idx]} (pos {min_idx})")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"Elemento {arr[i]} ya está en posición correcta")
        
        print(f"Estado actual: {arr}")
    
    print(f"\n Array final ordenado: {arr}")

def performance_test():
    """
    Prueba de rendimiento con diferentes tamaños de array
    """
    import time
    import random
    
    print("\n PRUEBA DE RENDIMIENTO")
    print("=" * 50)
    
    sizes = [100, 500, 1000, 2000, 5000]
    
    print(f"{'Tamaño':<8} {'Tiempo (s)':<12} {'Comparaciones':<15}")
    print("-" * 40)
    
    for size in sizes:
        # Generar array aleatorio
        test_array = [random.randint(1, 10000) for _ in range(size)]
        
        # Medir tiempo
        start_time = time.time()
        selection_sort(test_array.copy())
        end_time = time.time()
        
        execution_time = end_time - start_time
        # Número teórico de comparaciones: n(n-1)/2
        comparisons = size * (size - 1) // 2
        
        print(f"{size:<8} {execution_time:<12.6f} {comparisons:<15,}")

def comparison_with_builtin():
    """
    Comparación con la función sorted() de Python
    """
    import time
    import random
    
    print("\n🔍 COMPARACIÓN CON sorted() DE PYTHON")
    print("=" * 55)
    
    test_array = [random.randint(1, 10000) for _ in range(2000)]
    
    # Medir selection sort
    start_time = time.time()
    selection_result = selection_sort(test_array.copy())
    selection_time = time.time() - start_time
    
    # Medir sorted() de Python
    start_time = time.time()
    python_result = sorted(test_array.copy())
    python_time = time.time() - start_time
    
    print(f"Selection Sort: {selection_time:.6f} segundos")
    print(f"Python sorted(): {python_time:.6f} segundos")
    print(f"Velocidad relativa: {python_time/selection_time*100:.1f}% del tiempo")
    print(f"¿Resultados iguales? {selection_result == python_result}")

def test_descending_order():
    """
    Prueba del ordenamiento descendente
    """
    print("\n PRUEBA DE ORDENAMIENTO DESCENDENTE")
    print("=" * 50)
    
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],
        [5, -2, 0, -8, 3]
    ]
    
    for i, test_array in enumerate(test_cases, 1):
        print(f"\nCaso {i}:")
        print(f"  Original:  {test_array}")
        
        result = selection_sort_desc(test_array.copy())
        expected = sorted(test_array, reverse=True)
        
        print(f"  Resultado: {result}")
        print(f"  Esperado:  {expected}")
        print(f"  ¿Correcto? {result == expected}")

def analyze_complexity():
    """
    Análisis de la complejidad del algoritmo
    """
    print("\n ANÁLISIS DE COMPLEJIDAD")
    print("=" * 50)
    
    print("""
    COMPLEJIDAD TEMPORAL:
    - Mejor caso:    O(n²) - Siempre realiza n(n-1)/2 comparaciones
    - Caso promedio: O(n²) - Independiente del orden inicial
    - Peor caso:     O(n²) - Siempre realiza n(n-1)/2 comparaciones
    
    COMPLEJIDAD ESPACIAL:
    - O(1) - Ordenamiento in-place, no requiere memoria adicional
    
    CARACTERÍSTICAS:
    - No adaptativo: No mejora con arrays parcialmente ordenados
    - Inestable: Puede cambiar el orden relativo de elementos iguales
    - Poco intercambios: Máximo n intercambios
    - Útil para arrays pequeños o cuando los intercambios son costosos
    """)

def stability_test():
    """
    Prueba para verificar si el algoritmo es estable
    """
    print("\n PRUEBA DE ESTABILIDAD")
    print("=" * 50)
    
    # Array con elementos que tienen el mismo valor pero diferente "identidad"
    class Element:
        def __init__(self, value, id):
            self.value = value
            self.id = id
        
        def __lt__(self, other):
            return self.value < other.value
        
        def __repr__(self):
            return f"({self.value}-{self.id})"
    
    # Crear array con elementos duplicados pero diferentes IDs
    arr = [Element(5, 1), Element(2, 1), Element(5, 2), Element(3, 1), Element(2, 2)]
    
    print("Array original:")
    for elem in arr:
        print(f"  {elem}")
    
    # Ordenar por valor
    sorted_arr = selection_sort(arr.copy())
    
    print("\nArray ordenado:")
    for elem in sorted_arr:
        print(f"  {elem}")
    
    # Verificar estabilidad
    print("\n¿El algoritmo es estable?")
    print("En Selection Sort, NO es estable porque los intercambios")
    print("pueden alterar el orden relativo de elementos iguales.")

# Ejecutar todas las pruebas
if __name__ == "__main__":
    # Ejecutar pruebas principales
    test_selection_sort()
    
    # Demostración visual
    visual_selection_sort_demo()
    
    # Prueba de orden descendente
    test_descending_order()
    
    # Análisis de complejidad
    analyze_complexity()
    
    # Prueba de estabilidad
    stability_test()
    
    # Pruebas de rendimiento
    performance_test()
    comparison_with_builtin()
    
    # Demostración extra detallada
    print("\n" + "=" * 60)
    print(" DEMOSTRACIÓN EXTRA DETALLADA")
    print("=" * 60)
    test_array = [29, 10, 14, 37, 13]
    selection_sort_verbose(test_array.copy())