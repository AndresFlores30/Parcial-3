def natural_merge_sort(arr):
    """
    Natural Merging - Ordenamiento por fusion natural
    Detecta secuencias naturales ordenadas en los datos
    """
    if len(arr) <= 1:
        return arr
    
    # Detectar secuencias naturales ordenadas
    secuencias = detectar_secuencias_naturales(arr)
    print("Secuencias naturales detectadas:", secuencias)
    print()
    
    # Distribuir secuencias alternadamente entre dos archivos
    archivo1 = []
    archivo2 = []
    
    for i, secuencia in enumerate(secuencias):
        if i % 2 == 0:
            archivo1.append(secuencia)
        else:
            archivo2.append(secuencia)
    
    print("Distribucion inicial:")
    print(f"Archivo 1: {archivo1}")
    print(f"Archivo 2: {archivo2}")
    print()
    
    # Fusionar hasta tener una sola secuencia
    paso = 1
    while len(archivo1) > 1 or len(archivo2) > 1:
        print(f"Paso {paso} de fusion:")
        archivo1, archivo2 = fusionar_paso_natural(archivo1, archivo2)
        paso += 1
    
    # Obtener resultado final
    if archivo1:
        resultado = archivo1[0]
    else:
        resultado = archivo2[0]
    
    return resultado

def detectar_secuencias_naturales(arr):
    """
    Detecta secuencias naturalmente ordenadas en el array
    """
    if not arr:
        return []
    
    secuencias = []
    secuencia_actual = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            # Continua la secuencia ascendente
            secuencia_actual.append(arr[i])
        else:
            # Fin de secuencia, empezar nueva
            secuencias.append(secuencia_actual)
            secuencia_actual = [arr[i]]
    
    # Agregar la ultima secuencia
    secuencias.append(secuencia_actual)
    
    return secuencias

def fusionar_paso_natural(archivo1, archivo2):
    """
    Realiza un paso de fusion natural
    """
    nuevo_archivo1 = []
    nuevo_archivo2 = []
    
    # Fusionar secuencias mientras ambos archivos tengan datos
    while archivo1 and archivo2:
        secuencia1 = archivo1.pop(0)
        secuencia2 = archivo2.pop(0)
        
        secuencia_fusionada = fusionar_secuencias(secuencia1, secuencia2)
        print(f"  Fusionar {secuencia1} + {secuencia2} = {secuencia_fusionada}")
        
        # Alternar entre los nuevos archivos
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia_fusionada)
        else:
            nuevo_archivo2.append(secuencia_fusionada)
    
    # Agregar secuencias restantes
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
    
    print(f"Archivo 1 despues del paso: {nuevo_archivo1}")
    print(f"Archivo 2 despues del paso: {nuevo_archivo2}")
    print()
    
    return nuevo_archivo1, nuevo_archivo2

def fusionar_secuencias(seq1, seq2):
    """
    Fusiona dos secuencias ordenadas
    """
    resultado = []
    i = j = 0
    
    while i < len(seq1) and j < len(seq2):
        if seq1[i] <= seq2[j]:
            resultado.append(seq1[i])
            i += 1
        else:
            resultado.append(seq2[j])
            j += 1
    
    # Agregar elementos restantes
    resultado.extend(seq1[i:])
    resultado.extend(seq2[j:])
    
    return resultado

def natural_merge_detallado(arr):
    """
    Version detallada del Natural Merging
    """
    print("PROCESO NATURAL MERGING")
    print("======================")
    print(f"Array original: {arr}")
    print()
    
    if len(arr) <= 1:
        return arr
    
    # Fase 1: Deteccion de secuencias naturales
    print("FASE 1: DETECCION DE SECUENCIAS NATURALES")
    print("----------------------------------------")
    
    secuencias = []
    secuencia_actual = [arr[0]]
    print(f"Iniciando secuencia: [{arr[0]}]")
    
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            secuencia_actual.append(arr[i])
            print(f"  {arr[i]} >= {arr[i-1]} - Agregar a secuencia actual: {secuencia_actual}")
        else:
            secuencias.append(secuencia_actual)
            print(f"  {arr[i]} < {arr[i-1]} - Fin de secuencia: {secuencia_actual}")
            secuencia_actual = [arr[i]]
            print(f"  Nueva secuencia: {secuencia_actual}")
    
    secuencias.append(secuencia_actual)
    print(f"  Ultima secuencia: {secuencia_actual}")
    
    print(f"\nSecuencias naturales encontradas: {secuencias}")
    print()
    
    # Fase 2: Distribucion
    print("FASE 2: DISTRIBUCION")
    print("-------------------")
    
    archivo1 = []
    archivo2 = []
    
    for i, secuencia in enumerate(secuencias):
        if i % 2 == 0:
            archivo1.append(secuencia)
            print(f"Secuencia {i+1}: {secuencia} -> Archivo 1")
        else:
            archivo2.append(secuencia)
            print(f"Secuencia {i+1}: {secuencia} -> Archivo 2")
    
    print(f"\nEstado inicial:")
    print(f"Archivo 1: {archivo1}")
    print(f"Archivo 2: {archivo2}")
    print()
    
    # Fase 3: Fusion
    paso = 1
    while len(archivo1) > 1 or len(archivo2) > 1:
        print(f"FASE 3: FUSION - PASO {paso}")
        print("-------------------")
        
        archivo1, archivo2 = fusionar_paso_detallado(archivo1, archivo2)
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

def fusionar_paso_detallado(archivo1, archivo2):
    """
    Paso de fusion con detalles
    """
    nuevo_archivo1 = []
    nuevo_archivo2 = []
    
    print("Proceso de fusion:")
    
    fusion_count = 0
    while archivo1 and archivo2:
        secuencia1 = archivo1.pop(0)
        secuencia2 = archivo2.pop(0)
        
        secuencia_fusionada = fusionar_secuencias(secuencia1, secuencia2)
        fusion_count += 1
        print(f"  Fusion {fusion_count}:")
        print(f"    Secuencia 1: {secuencia1}")
        print(f"    Secuencia 2: {secuencia2}")
        print(f"    Resultado: {secuencia_fusionada}")
        
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia_fusionada)
            print(f"    -> Archivo 1")
        else:
            nuevo_archivo2.append(secuencia_fusionada)
            print(f"    -> Archivo 2")
    
    # Procesar secuencias restantes
    while archivo1:
        secuencia = archivo1.pop(0)
        print(f"  Secuencia restante de Archivo 1: {secuencia}")
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia)
            print(f"    -> Archivo 1")
        else:
            nuevo_archivo2.append(secuencia)
            print(f"    -> Archivo 2")
    
    while archivo2:
        secuencia = archivo2.pop(0)
        print(f"  Secuencia restante de Archivo 2: {secuencia}")
        if len(nuevo_archivo1) <= len(nuevo_archivo2):
            nuevo_archivo1.append(secuencia)
            print(f"    -> Archivo 1")
        else:
            nuevo_archivo2.append(secuencia)
            print(f"    -> Archivo 2")
    
    print(f"\nEstado despues del paso:")
    print(f"Archivo 1: {nuevo_archivo1}")
    print(f"Archivo 2: {nuevo_archivo2}")
    print()
    
    return nuevo_archivo1, nuevo_archivo2

def ejemplo_simple():
    """
    Ejemplo conceptual simple
    """
    print("EJEMPLO CONCEPTUAL")
    print("=================")
    
    arr = [5, 8, 12, 3, 7, 9, 2, 6]
    print(f"Array: {arr}")
    print()
    
    print("Deteccion de secuencias naturales:")
    print("  [5, 8, 12]  (5->8->12: ascendente)")
    print("  [3, 7, 9]   (3->7->9: ascendente)") 
    print("  [2, 6]      (2->6: ascendente)")
    print()
    
    print("Distribucion:")
    print("  Archivo 1: [5, 8, 12], [2, 6]")
    print("  Archivo 2: [3, 7, 9]")
    print()
    
    print("Paso 1 de fusion:")
    print("  Fusionar [5,8,12] + [3,7,9] = [3,5,7,8,9,12] -> Archivo 1")
    print("  [2,6] sobra -> Archivo 2")
    print()
    
    print("Paso 2 de fusion:")
    print("  Fusionar [3,5,7,8,9,12] + [2,6] = [2,3,5,6,7,8,9,12]")
    print()
    
    print("Resultado final: [2, 3, 5, 6, 7, 8, 9, 12]")

def prueba_natural_merge():
    """
    Pruebas del algoritmo
    """
    print("PRUEBAS NATURAL MERGING")
    print("======================")
    
    pruebas = [
        [1, 3, 5, 2, 4, 6, 8, 7],  # Secuencias: [1,3,5], [2,4,6,8], [7]
        [9, 8, 7, 6, 5],           # Secuencias: [9], [8], [7], [6], [5]
        [1, 2, 3, 4, 5],           # Secuencias: [1,2,3,4,5]
        [5, 4, 3, 2, 1],           # Secuencias: [5], [4], [3], [2], [1]
        [10, 20, 5, 15, 25, 30],   # Secuencias: [10,20], [5,15,25,30]
        [42],                       # Secuencias: [42]
        []                          # Secuencias: []
    ]
    
    for i, arr in enumerate(pruebas, 1):
        print(f"\nPrueba {i}: {arr}")
        resultado = natural_merge_sort(arr)
        print(f"Ordenado: {resultado}")

def explicar_natural_merge():
    """
    Explica el algoritmo Natural Merging
    """
    print("\nCOMO FUNCIONA NATURAL MERGING")
    print("============================")
    print("1. DETECCION DE SECUENCIAS NATURALES:")
    print("   - Recorrer el array detectando secuencias ascendentes")
    print("   - Una secuencia termina cuando el siguiente elemento es menor")
    print("   - Aprovecha el orden natural que ya existe en los datos")
    print()
    print("2. DISTRIBUCION:")
    print("   - Distribuir secuencias alternadamente entre dos archivos")
    print("   - Secuencia 1 -> Archivo 1, Secuencia 2 -> Archivo 2, etc.")
    print()
    print("3. FUSION:")
    print("   - Fusionar primera secuencia de Archivo1 con primera de Archivo2")
    print("   - Fusionar segunda secuencia de Archivo1 con segunda de Archivo2")
    print("   - Alternar resultados entre los archivos")
    print("   - Repetir hasta tener una sola secuencia ordenada")
    print()
    print("4. VENTAJAS:")
    print("   - Mas eficiente cuando los datos tienen secuencias ordenadas")
    print("   - Menos pasos de fusion que Straight Merging")
    print("   - Ideal para datos parcialmente ordenados")

# Programa principal
if __name__ == "__main__":
    # Ejemplo detallado
    print("=" * 60)
    arr = [15, 20, 25, 5, 10, 30, 2, 8, 12]
    natural_merge_detallado(arr)
    
    # Ejemplo conceptual
    print("\n" + "=" * 60)
    ejemplo_simple()
    
    # Pruebas
    print("\n" + "=" * 60)
    prueba_natural_merge()
    
    # Explicacion
    print("\n" + "=" * 60)
    explicar_natural_merge()
    
    # Ejemplo final
    print("\n" + "=" * 60)
    print("EJEMPLO FINAL")
    print("=============")
    arr_final = [40, 45, 50, 20, 25, 35, 10, 15]
    print(f"Array: {arr_final}")
    resultado = natural_merge_sort(arr_final)
    print(f"Ordenado: {resultado}")