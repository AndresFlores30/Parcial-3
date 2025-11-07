def counting_sort_para_radix(arr, exp):
    """
    Counting sort modificado para RadixSort
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Contar ocurrencias de cada digito
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Cambiar count[i] para que contenga la posicion real
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir el array de salida
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    # Copiar el array de salida al original
    for i in range(n):
        arr[i] = output[i]

def radixsort(arr):
    """
    Ordenamiento RadixSort
    """
    if len(arr) <= 1:
        return arr
    
    # Encontrar el numero maximo para saber el numero de digitos
    max_num = max(arr)
    
    # Aplicar counting sort para cada digito
    exp = 1
    while max_num // exp > 0:
        counting_sort_para_radix(arr, exp)
        exp *= 10
    
    return arr

def radixsort_detallado(arr):
    """
    Version que muestra el proceso paso a paso
    """
    if len(arr) <= 1:
        return arr
    
    print("Array original:", arr)
    max_num = max(arr)
    print("Numero maximo:", max_num)
    print("Numero de digitos:", len(str(max_num)))
    print()
    
    exp = 1
    paso = 1
    
    while max_num // exp > 0:
        print(f"Paso {paso} - Ordenando por digito en posicion {exp}:")
        print(f"  Digito actual: unidades de {exp}")
        
        # Mostrar como se calculan los digitos
        print("  Calculando digitos:")
        for num in arr:
            digito = (num // exp) % 10
            print(f"    {num} -> digito: {digito}")
        
        # Aplicar counting sort
        counting_sort_para_radix(arr, exp)
        
        print(f"  Array despues del paso: {arr}")
        print()
        
        exp *= 10
        paso += 1
    
    return arr

def mostrar_proceso_radix():
    """
    Muestra el proceso completo de RadixSort
    """
    print("PROCESO DE RADIXSORT")
    print("===================")
    
    arr = [170, 45, 75, 90, 2, 802, 24, 66]
    resultado = radixsort_detallado(arr.copy())
    
    print(f"Array final ordenado: {resultado}")

def prueba_radixsort():
    """
    Pruebas basicas del algoritmo
    """
    print("PRUEBAS DE RADIXSORT")
    print("===================")
    
    pruebas = [
        [170, 45, 75, 90, 2, 802, 24, 66],
        [10, 5, 100, 1, 50],
        [321, 123, 231, 312, 132],
        [9, 8, 7, 6, 5],
        [1000, 100, 10, 1],
        [42],
        []
    ]
    
    for i, arr in enumerate(pruebas, 1):
        print(f"\nPrueba {i}: {arr}")
        resultado = radixsort(arr.copy())
        print(f"Ordenado: {resultado}")

def ejemplo_digitos():
    """
    Ejemplo de como se obtienen los digitos
    """
    print("EJEMPLO DE EXTRACCION DE DIGITOS")
    print("================================")
    
    numero = 345
    print(f"Numero: {numero}")
    print(f"Unidades: ({numero} // 1) % 10 = { (345 // 1) % 10 }")
    print(f"Decenas:  ({numero} // 10) % 10 = { (345 // 10) % 10 }")
    print(f"Centenas: ({numero} // 100) % 10 = { (345 // 100) % 10 }")
    
    print("\nPara el numero 67:")
    print(f"Unidades: (67 // 1) % 10 = { (67 // 1) % 10 }")
    print(f"Decenas:  (67 // 10) % 10 = { (67 // 10) % 10 }")
    print(f"Centenas: (67 // 100) % 10 = { (67 // 100) % 10 }")

def ejemplo_simple():
    """
    Ejemplo muy simple paso a paso
    """
    print("\nEJEMPLO SIMPLE PASO A PASO")
    print("=========================")
    
    arr = [23, 12, 45, 1]
    print(f"Array inicial: {arr}")
    
    # Paso 1: ordenar por unidades
    print("\nPaso 1 - Ordenar por unidades:")
    unidades = [(num, (num // 1) % 10) for num in arr]
    print(f"  Numeros y sus unidades: {unidades}")
    arr_ordenado_unidades = sorted(arr, key=lambda x: (x // 1) % 10)
    print(f"  Ordenado por unidades: {arr_ordenado_unidades}")
    
    # Paso 2: ordenar por decenas
    print("\nPaso 2 - Ordenar por decenas:")
    decenas = [(num, (num // 10) % 10) for num in arr_ordenado_unidades]
    print(f"  Numeros y sus decenas: {decenas}")
    arr_ordenado_final = sorted(arr_ordenado_unidades, key=lambda x: (x // 10) % 10)
    print(f"  Ordenado por decenas: {arr_ordenado_final}")

def comparar_con_python():
    """
    Compara con la funcion sorted de Python
    """
    print("\nCOMPARACION CON PYTHON")
    print("=====================")
    
    arr = [100, 5, 25, 150, 1, 75]
    print(f"Array: {arr}")
    
    radix_result = radixsort(arr.copy())
    python_result = sorted(arr)
    
    print(f"RadixSort: {radix_result}")
    print(f"Python: {python_result}")
    print(f"Son iguales: {radix_result == python_result}")

def explicar_radixsort():
    """
    Explica como funciona el algoritmo
    """
    print("\nCOMO FUNCIONA RADIXSORT")
    print("======================")
    print("1. Encontrar el numero con mas digitos")
    print("2. Para cada digito (de menos a mas significativo):")
    print("   - Usar Counting Sort para ordenar por ese digito")
    print("   - Empezar por las unidades, luego decenas, etc.")
    print("3. Caracteristicas:")
    print("   - Ordena numeros enteros no negativos")
    print("   - Complejidad: O(d * n) donde d es el numero de digitos")
    print("   - Estable: mantiene el orden relativo de elementos iguales")
    print("   - No funciona con numeros negativos sin modificacion")

# Programa principal
if __name__ == "__main__":
    # Ejemplo principal
    mostrar_proceso_radix()
    
    # Ejemplo de extraccion de digitos
    ejemplo_digitos()
    
    # Ejemplo simple
    ejemplo_simple()
    
    # Pruebas basicas
    prueba_radixsort()
    
    # Comparacion
    comparar_con_python()
    
    # Explicacion
    explicar_radixsort()
    
    # Ejemplo final
    print("\nEJEMPLO FINAL")
    print("=============")
    arr_final = [543, 12, 8, 99, 1000, 76]
    print(f"Array: {arr_final}")
    resultado_final = radixsort(arr_final.copy())
    print(f"Ordenado: {resultado_final}")