def insertion_sort(arr):
    """
    Ordenamiento por Inserción
    Complejidad: O(n²) en peor caso, O(n) en mejor caso (cuando ya está ordenado)
    """
    # Iterar desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento actual a insertar
        j = i - 1     # Índice del elemento anterior
        
        # Mover elementos mayores que key una posición adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertar key en la posición correcta
        arr[j + 1] = key
    
    return arr

def insertion_sort_desc(arr):
    """
    Ordenamiento por Inserción en orden descendente
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover elementos menores que key una posición adelante
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def test_insertion_sort():
    """
    Función completa de pruebas para el método de inserción
    """
    print("🔍 PRUEBAS DEL MÉTODO DE ORDENAMIENTO POR INSERCIÓN")
    print("=" * 60)
    
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
        result = insertion_sort(input_copy)
        
        print(f"   Expected: {test['expected']}")
        print(f"   Result:   {result}")
        
        # Verificar resultado
        if result == test['expected']:
            print("   * PASSED")
            passed_tests += 1
        else:
            print("   X FAILED")
    
    # Mostrar resumen
    print("\n" + "=" * 60)
    print(f" RESUMEN DE PRUEBAS: {passed_tests}/{total_tests} correctos")
    print(f" Porcentaje de éxito: { (passed_tests/total_tests)*100:.1f}%")

def visual_insertion_sort_demo():
    """
    Demostración visual paso a paso del algoritmo
    """
    print("\n DEMOSTRACIÓN VISUAL PASO A PASO")
    print("=" * 50)
    
    arr = [64, 34, 25, 12, 22]
    print(f"Array original: {arr}")
    print("\nProceso de ordenamiento:")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nIteración {i}: key = {key}")
        print(f"  Estado actual: {arr}")
        
        while j >= 0 and arr[j] > key:
            print(f"  Mover {arr[j]} de posición {j} a posición {j+1}")
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"  Insertar {key} en posición {j+1}")
        print(f"  Nuevo estado: {arr}")
    
    print(f"\n Array final ordenado: {arr}")

def performance_test():
    """
    Prueba de rendimiento con diferentes tamaños de array
    """
    import time
    import random
    
    print("\n PRUEBA DE RENDIMIENTO")
    print("=" * 50)
    
    sizes = [100, 500, 1000, 2000]
    
    for size in sizes:
        # Generar array aleatorio
        test_array = [random.randint(1, 10000) for _ in range(size)]
        
        # Medir tiempo
        start_time = time.time()
        insertion_sort(test_array.copy())
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Tamaño {size:4d} elementos: {execution_time:.6f} segundos")

def comparison_with_builtin():
    """
    Comparación con la función sorted() de Python
    """
    import time
    import random
    
    print("\n COMPARACIÓN CON sorted() DE PYTHON")
    print("=" * 50)
    
    test_array = [random.randint(1, 10000) for _ in range(1000)]
    
    # Medir insertion sort
    start_time = time.time()
    insertion_result = insertion_sort(test_array.copy())
    insertion_time = time.time() - start_time
    
    # Medir sorted() de Python
    start_time = time.time()
    python_result = sorted(test_array.copy())
    python_time = time.time() - start_time
    
    print(f"Insertion Sort: {insertion_time:.6f} segundos")
    print(f"Python sorted(): {python_time:.6f} segundos")
    print(f"¿Resultados iguales? {insertion_result == python_result}")

def test_descending_order():
    """
    Prueba del ordenamiento descendente
    """
    print("\n PRUEBA DE ORDENAMIENTO DESCENDENTE")
    print("=" * 50)
    
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Array original: {test_array}")
    
    result = insertion_sort_desc(test_array.copy())
    print(f"Array descendente: {result}")
    
    expected = [90, 64, 34, 25, 22, 12, 11]
    print(f"¿Correcto? {result == expected}")

# Ejecutar todas las pruebas
if __name__ == "__main__":
    # Ejecutar pruebas principales
    test_insertion_sort()
    
    # Demostración visual
    visual_insertion_sort_demo()
    
    # Prueba de orden descendente
    test_descending_order()
    
    # Pruebas de rendimiento (comentar si no se quieren ejecutar)
    performance_test()
    comparison_with_builtin()