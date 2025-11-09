def balanced_multiway_merge(arr, k=3):
    """
    Balanced Multiway Merging con k archivos
    """
    if len(arr) <= 1:
        return arr
    
    # Crear k archivos iniciales
    archivos = [[] for _ in range(k)]
    
    # Distribuir elementos en los archivos (round-robin)
    for i, elemento in enumerate(arr):
        archivo_idx = i % k
        archivos[archivo_idx].append([elemento])  # Cada elemento es una secuencia
    
    print(f"Distribucion inicial en {k} archivos:")
    for i, archivo in enumerate(archivos):
        print(f"  Archivo {i+1}: {archivo}")
    print()
    
    # Fusionar hasta que solo quede una secuencia
    paso = 1
    while sum(len(archivo) for archivo in archivos) > 1:
        print(f"Paso {paso} de fusion:")
        archivos = fusionar_paso_multiway(archivos, k)
        paso += 1
    
    # Encontrar el archivo que contiene el resultado
    for archivo in archivos:
        if archivo:
            return archivo[0]
    
    return []

def fusionar_paso_multiway(archivos, k):
    """
    Realiza un paso de fusion multiway
    """
    nuevos_archivos = [[] for _ in range(k)]
    archivo_actual = 0
    
    # Tomar una secuencia de cada archivo y fusionarlas
    while any(archivos):  # Mientras haya secuencias en algun archivo
        secuencias_a_fusionar = []
        
        # Tomar una secuencia de cada archivo no vacio
        for i in range(k):
            if archivos[i]:
                secuencia = archivos[i].pop(0)
                secuencias_a_fusionar.append(secuencia)
        
        if secuencias_a_fusionar:
            # Fusionar todas las secuencias
            secuencia_fusionada = fusionar_multiway(secuencias_a_fusionar)
            print(f"  Fusionar {secuencias_a_fusionar} = {secuencia_fusionada}")
            
            # Colocar en el siguiente archivo disponible
            nuevos_archivos[archivo_actual].append(secuencia_fusionada)
            archivo_actual = (archivo_actual + 1) % k
    
    print(f"  Estado despues del paso:")
    for i, archivo in enumerate(nuevos_archivos):
        print(f"    Archivo {i+1}: {archivo}")
    print()
    
    return nuevos_archivos

def fusionar_multiway(secuencias):
    """
    Fusiona multiples secuencias ordenadas
    """
    if not secuencias:
        return []
    
    resultado = []
    indices = [0] * len(secuencias)
    
    while True:
        # Encontrar el menor elemento entre las secuencias
        min_valor = None
        min_idx = -1
        
        for i, secuencia in enumerate(secuencias):
            if indices[i] < len(secuencia):
                if min_valor is None or secuencia[indices[i]] < min_valor:
                    min_valor = secuencia[indices[i]]
                    min_idx = i
        
        if min_valor is None:
            break  # Todas las secuencias procesadas
        
        resultado.append(min_valor)
        indices[min_idx] += 1
    
    return resultado

def balanced_multiway_detallado(arr, k=3):
    """
    Version detallada del Balanced Multiway Merging
    """
    print("PROCESO BALANCED MULTIWAY MERGING")
    print("================================")
    print(f"Array original: {arr}")
    print(f"Numero de archivos (k): {k}")
    print()
    
    if len(arr) <= 1:
        return arr
    
    # Fase 1: Distribucion
    print("FASE 1: DISTRIBUCION")
    print("-------------------")
    
    archivos = [[] for _ in range(k)]
    
    for i, elemento in enumerate(arr):
        archivo_idx = i % k
        archivos[archivo_idx].append([elemento])
        print(f"Elemento {elemento} -> Archivo {archivo_idx + 1}")
    
    print(f"\nEstado inicial:")
    for i, archivo in enumerate(archivos):
        print(f"  Archivo {i+1}: {archivo}")
    print()
    
    # Fase 2: Fusion
    paso = 1
    total_secuencias = sum(len(archivo) for archivo in archivos)
    
    while total_secuencias > 1:
        print(f"FASE 2: FUSION - PASO {paso}")
        print("-------------------")
        print(f"Secuencias antes del paso: {total_secuencias}")
        
        archivos = fusionar_paso_detallado(archivos, k)
        
        total_secuencias = sum(len(archivo) for archivo in archivos)
        print(f"Secuencias despues del paso: {total_secuencias}")
        print()
        paso += 1
    
    # Resultado final
    for i, archivo in enumerate(archivos):
        if archivo:
            resultado = archivo[0]
            print(f"RESULTADO FINAL (del Archivo {i+1}): {resultado}")
            return resultado
    
    return []

def fusionar_paso_detallado(archivos, k):
    """
    Paso de fusion con detalles
    """
    nuevos_archivos = [[] for _ in range(k)]
    archivo_actual = 0
    fusion_count = 0
    
    print("Proceso de fusion:")
    
    while any(archivos):
        secuencias_a_fusionar = []
        archivos_utilizados = []
        
        # Recolectar una secuencia de cada archivo no vacio
        for i in range(k):
            if archivos[i]:
                secuencia = archivos[i].pop(0)
                secuencias_a_fusionar.append(secuencia)
                archivos_utilizados.append(i + 1)
        
        if secuencias_a_fusionar:
            fusion_count += 1
            print(f"  Fusion {fusion_count}:")
            print(f"    Secuencias de archivos {archivos_utilizados}: {secuencias_a_fusionar}")
            
            secuencia_fusionada = fusionar_multiway(secuencias_a_fusionar)
            print(f"    Resultado: {secuencia_fusionada}")
            
            nuevos_archivos[archivo_actual].append(secuencia_fusionada)
            print(f"    -> Archivo {archivo_actual + 1}")
            
            archivo_actual = (archivo_actual + 1) % k
    
    return nuevos_archivos

def ejemplo_simple_k2():
    """
    Ejemplo simple con k=2 (como el merge normal)
    """
    print("EJEMPLO CON k=2 (COMPARACION CON TWO-WAY MERGE)")
    print("==============================================")
    
    arr = [15, 8, 23, 4, 42]
    print(f"Array: {arr}")
    
    resultado = balanced_multiway_merge(arr, k=2)
    print(f"Resultado: {resultado}")

def ejemplo_simple_k3():
    """
    Ejemplo simple con k=3
    """
    print("\nEJEMPLO CON k=3")
    print("==============")
    
    arr = [25, 10, 35, 5, 20, 30, 15, 40]
    print(f"Array: {arr}")
    
    resultado = balanced_multiway_merge(arr, k=3)
    print(f"Resultado: {resultado}")

def prueba_multiway():
    """
    Pruebas con diferentes valores de k
    """
    print("PRUEBAS CON DIFERENTES VALORES DE k")
    print("==================================")
    
    arr = [12, 5, 18, 3, 9, 15, 7, 20, 1]
    
    for k in [2, 3, 4]:
        print(f"\nk = {k}:")
        resultado = balanced_multiway_merge(arr.copy(), k)
        print(f"Ordenado: {resultado}")

def explicar_multiway():
    """
    Explica el algoritmo Balanced Multiway Merging
    """
    print("\nCOMO FUNCIONA BALANCED MULTIWAY MERGING")
    print("======================================")
    print("1. DISTRIBUCION:")
    print("   - Usar k archivos en lugar de 2")
    print("   - Distribucion round-robin (elemento i -> archivo i mod k)")
    print("   - Cada elemento forma una secuencia ordenada de longitud 1")
    print()
    print("2. FUSION MULTIWAY:")
    print("   - En cada paso, tomar una secuencia de cada archivo")
    print("   - Fusionar las k secuencias en una sola")
    print("   - Distribuir resultados round-robin en los k archivos")
    print("   - Repetir hasta tener una sola secuencia")
    print()
    print("3. VENTAJAS:")
    print("   - Menos pasos de fusion que two-way merging")
    print("   - Log_k(n) pasos en lugar de log_2(n) pasos")
    print("   - Mas eficiente para grandes volumenes de datos")
    print("   - Ideal para ordenamiento externo con multiples dispositivos")
    print()
    print("4. COMPLEJIDAD:")
    print("   - Numero de pasos: O(log_k n)")
    print("   - Operaciones por paso: O(n)")
    print("   - Total: O(n log_k n)")

# Programa principal
if __name__ == "__main__":
    # Ejemplo detallado
    print("=" * 60)
    arr = [30, 10, 25, 5, 20, 15, 35, 8]
    balanced_multiway_detallado(arr, k=3)
    
    # Ejemplos simples
    print("\n" + "=" * 60)
    ejemplo_simple_k2()
    ejemplo_simple_k3()
    
    # Pruebas con diferentes k
    print("\n" + "=" * 60)
    prueba_multiway()
    
    # Explicacion
    print("\n" + "=" * 60)
    explicar_multiway()
    
    # Ejemplo final
    print("\n" + "=" * 60)
    print("EJEMPLO FINAL CON k=4")
    print("====================")
    arr_final = [45, 12, 67, 23, 89, 34, 56, 78, 90, 11]
    print(f"Array: {arr_final}")
    resultado = balanced_multiway_merge(arr_final, k=4)
    print(f"Ordenado: {resultado}")