def straight_merge_sort(arr):
    """
    Straight Merging - Ordenamiento por fusion directa
    Simula el ordenamiento externo usando memoria interna
    """
    if len(arr) <= 1:
        return arr
    
    # Dividir el array en dos archivos (listas) simulados
    archivo1 = []
    archivo2 = []
    
    # Distribucion inicial alternada
    for i, elemento in enumerate(arr):
        if i % 2 == 0:
            archivo1.append([elemento])  # Cada elemento es una secuencia ordenada
        else:
            archivo2.append([elemento])
    
    print("Distribucion inicial:")
    print(f"Archivo 1: {archivo1}")
    print(f"Archivo 2: {archivo2}")
    print()
    
    # Fusionar hasta tener una sola secuencia ordenada
    while len(archivo1) > 1 or len(archivo2) > 1:
        archivo1, archivo2 = fusionar_paso(archivo1, archivo2)
    
    # Obtener el resultado final
    if archivo1:
        resultado = archivo1[0]
    else:
        resultado = archivo2[0]
    
    return resultado

def fusionar_paso(archivo1, archivo2):
    """
    Realiza un paso de fusion entre dos archivos
    """
    nuevo_archivo1 = []
    nuevo_archivo2 = []
    
    print("Fusionando secuencias:")
    
    # Fusionar secuencias de ambos archivos
    while archivo1 and archivo2:
        # Tomar una secuencia de cada archivo y fusionarlas
        secuencia1 = archivo1.pop(0)
        secuencia2 = archivo2.pop(0)
        
        secuencia_fusionada = fusionar(secuencia1, secuencia2)
        print(f"  Fusionar {secuencia1} + {secuencia2} = {secuencia_fusionada}")
        
        # Alternar entre los nuevos archivos
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia_fusionada)
        else:
            nuevo_archivo2.append(secuencia_fusionada)
    
    # Agregar secuencias restantes
    while archivo1:
        secuencia = archivo1.pop(0)
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia)
        else:
            nuevo_archivo2.append(secuencia)
    
    while archivo2:
        secuencia = archivo2.pop(0)
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia)
        else:
            nuevo_archivo2.append(secuencia)
    
    print(f"Nuevo Archivo 1: {nuevo_archivo1}")
    print(f"Nuevo Archivo 2: {nuevo_archivo2}")
    print()
    
    return nuevo_archivo1, nuevo_archivo2

def fusionar(secuencia1, secuencia2):
    """
    Fusiona dos secuencias ordenadas en una sola
    """
    resultado = []
    i = j = 0
    
    while i < len(secuencia1) and j < len(secuencia2):
        if secuencia1[i] <= secuencia2[j]:
            resultado.append(secuencia1[i])
            i += 1
        else:
            resultado.append(secuencia2[j])
            j += 1
    
    # Agregar elementos restantes
    while i < len(secuencia1):
        resultado.append(secuencia1[i])
        i += 1
    
    while j < len(secuencia2):
        resultado.append(secuencia2[j])
        j += 1
    
    return resultado

def straight_merge_detallado(arr):
    """
    Version detallada que muestra todo el proceso
    """
    print("PROCESO STRAIGHT MERGING")
    print("=======================")
    print(f"Array original: {arr}")
    print()
    
    if len(arr) <= 1:
        return arr
    
    # Fase de distribucion
    archivo1 = []
    archivo2 = []
    
    print("FASE 1: DISTRIBUCION")
    print("-------------------")
    for i, elemento in enumerate(arr):
        if i % 2 == 0:
            archivo1.append([elemento])
            print(f"Elemento {elemento} -> Archivo 1")
        else:
            archivo2.append([elemento])
            print(f"Elemento {elemento} -> Archivo 2")
    
    print(f"\nEstado inicial:")
    print(f"Archivo 1: {archivo1}")
    print(f"Archivo 2: {archivo2}")
    print()
    
    # Fase de fusion
    paso = 1
    while len(archivo1) > 1 or len(archivo2) > 1:
        print(f"FASE 2: FUSION - PASO {paso}")
        print("-------------------")
        
        archivo1, archivo2 = fusionar_paso_detallado(archivo1, archivo2, paso)
        paso += 1
    
    # Resultado final
    if archivo1:
        resultado = archivo1[0]
    else:
        resultado = archivo2[0]
    
    print("RESULTADO FINAL")
    print("---------------")
    print(f"Array ordenado: {resultado}")
    
    return resultado

def fusionar_paso_detallado(archivo1, archivo2, paso):
    """
    Paso de fusion con detalles
    """
    nuevo_archivo1 = []
    nuevo_archivo2 = []
    
    print(f"Longitud de secuencias en este paso: {2 ** (paso - 1)}")
    print("Proceso de fusion:")
    
    fusion_count = 0
    while archivo1 and archivo2:
        secuencia1 = archivo1.pop(0)
        secuencia2 = archivo2.pop(0)
        
        secuencia_fusionada = fusionar(secuencia1, secuencia2)
        fusion_count += 1
        print(f"  Fusion {fusion_count}: {secuencia1} + {secuencia2} = {secuencia_fusionada}")
        
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia_fusionada)
        else:
            nuevo_archivo2.append(secuencia_fusionada)
    
    # Procesar secuencias restantes
    while archivo1:
        secuencia = archivo1.pop(0)
        print(f"  Secuencia restante de Archivo 1: {secuencia}")
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia)
        else:
            nuevo_archivo2.append(secuencia)
    
    while archivo2:
        secuencia = archivo2.pop(0)
        print(f"  Secuencia restante de Archivo 2: {secuencia}")
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia)
        else:
            nuevo_archivo2.append(secuencia)
    
    print(f"\nEstado despues del paso {paso}:")
    print(f"Archivo 1: {nuevo_archivo1}")
    print(f"Archivo 2: {nuevo_archivo2}")
    print()
    
    return nuevo_archivo1, nuevo_archivo2

def ejemplo_simple():
    """
    Ejemplo muy simple para entender el concepto
    """
    print("EJEMPLO SIMPLE CONCEPTUAL")
    print("========================")
    
    arr = [5, 2, 8, 1, 9]
    print(f"Array: {arr}")
    print()
    
    print("Simulando archivos externos:")
    print("Archivo1: [5], [8], [9]  (elementos en posiciones pares)")
    print("Archivo2: [2], [1]       (elementos en posiciones impares)")
    print()
    
    print("Paso 1 de fusion:")
    print("Fusionar [5] + [2] = [2, 5] -> Archivo1")
    print("Fusionar [8] + [1] = [1, 8] -> Archivo2")
    print("[9] sobra -> Archivo1")
    print()
    
    print("Estado despues del paso 1:")
    print("Archivo1: [[2, 5], [9]]")
    print("Archivo2: [[1, 8]]")
    print()
    
    print("Paso 2 de fusion:")
    print("Fusionar [2, 5] + [1, 8] = [1, 2, 5, 8] -> Archivo1")
    print("[9] sobra -> Archivo2")
    print()
    
    print("Estado despues del paso 2:")
    print("Archivo1: [[1, 2, 5, 8]]")
    print("Archivo2: [[9]]")
    print()
    
    print("Paso 3 de fusion:")
    print("Fusionar [1, 2, 5, 8] + [9] = [1, 2, 5, 8, 9] -> Archivo1")
    print()
    
    print("Resultado final: [1, 2, 5, 8, 9]")

def prueba_straight_merge():
    """
    Pruebas del algoritmo
    """
    print("PRUEBAS STRAIGHT MERGING")
    print("=======================")
    
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
        resultado = straight_merge_sort(arr)
        print(f"Ordenado: {resultado}")

def explicar_straight_merge():
    """
    Explica el algoritmo Straight Merging
    """
    print("\nCOMO FUNCIONA STRAIGHT MERGING")
    print("=============================")
    print("1. FASE DE DISTRIBUCION:")
    print("   - Dividir los datos en dos archivos")
    print("   - Distribucion alternada (elemento 1->archivo1, elemento 2->archivo2, etc.)")
    print("   - Cada elemento forma una secuencia ordenada de longitud 1")
    print()
    print("2. FASE DE FUSION:")
    print("   - Mientras haya mas de una secuencia:")
    print("   a) Fusionar primera secuencia de archivo1 con primera de archivo2")
    print("   b) Fusionar segunda secuencia de archivo1 con segunda de archivo2")
    print("   c) Alternar los resultados entre los dos archivos")
    print("   d) Las secuencias se duplican en longitud en cada paso")
    print()
    print("3. CARACTERISTICAS:")
    print("   - Ordenamiento externo (para datos que no caben en memoria)")
    print("   - Usa solo dos archivos auxiliares")
    print("   - Estable: mantiene el orden relativo")
    print("   - Complejidad: O(n log n)")

# Programa principal
if __name__ == "__main__":
    # Ejemplo detallado
    arr = [38, 27, 43, 3, 9, 82, 10]
    straight_merge_detallado(arr)
    
    # Ejemplo conceptual
    print("\n" + "="*50)
    ejemplo_simple()
    
    # Pruebas
    print("\n" + "="*50)
    prueba_straight_merge()
    
    # Explicacion
    print("\n" + "="*50)
    explicar_straight_merge()
    
    # Ejemplo final simple
    print("\n" + "="*50)
    print("EJEMPLO FINAL")
    print("=============")
    arr_final = [15, 8, 23, 4, 42]
    print(f"Array: {arr_final}")
    resultado = straight_merge_sort(arr_final)
    print(f"Ordenado: {resultado}")