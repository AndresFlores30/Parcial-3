def distribucion_secuencias_iniciales(arr):
    """
    Distribucion simple de secuencias iniciales (runs)
    """
    if not arr:
        return []
    
    print("Array original:", arr)
    print()
    
    # Detectar secuencias naturales (runs)
    secuencias = []
    secuencia_actual = [arr[0]]
    
    print("Detectando secuencias naturales:")
    print(f"Inicio secuencia: {[arr[0]]}")
    
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            secuencia_actual.append(arr[i])
            print(f"  {arr[i]} >= {arr[i-1]} - Continuar secuencia: {secuencia_actual}")
        else:
            secuencias.append(secuencia_actual)
            print(f"  {arr[i]} < {arr[i-1]} - Fin secuencia: {secuencia_actual}")
            secuencia_actual = [arr[i]]
            print(f"  Nueva secuencia: {secuencia_actual}")
    
    secuencias.append(secuencia_actual)
    print(f"  Ultima secuencia: {secuencia_actual}")
    
    print(f"\nSecuencias encontradas: {secuencias}")
    return secuencias

def distribuir_en_archivos(secuencias, num_archivos=2):
    """
    Distribuir secuencias en archivos
    """
    print(f"\nDistribuyendo en {num_archivos} archivos:")
    
    archivos = [[] for _ in range(num_archivos)]
    
    for i, secuencia in enumerate(secuencias):
        archivo_idx = i % num_archivos
        archivos[archivo_idx].append(secuencia)
        print(f"Secuencia {i+1}: {secuencia} -> Archivo {archivo_idx + 1}")
    
    print(f"\nEstado final:")
    for i, archivo in enumerate(archivos):
        print(f"Archivo {i+1}: {archivo}")
    
    return archivos

def ejemplo_completo():
    """
    Ejemplo completo de distribucion de runs iniciales
    """
    print("DISTRIBUCION DE SECUENCIAS INICIALES")
    print("====================================")
    
    # Datos de ejemplo
    datos = [15, 20, 25, 5, 10, 30, 2, 8, 12, 35, 1, 6]
    
    # Paso 1: Detectar secuencias
    secuencias = distribucion_secuencias_iniciales(datos)
    
    # Paso 2: Distribuir en archivos
    archivos = distribuir_en_archivos(secuencias, 3)
    
    return archivos

def ejemplo_simple():
    """
    Ejemplo mas simple para entender el concepto
    """
    print("\n" + "="*50)
    print("EJEMPLO SIMPLE")
    print("==============")
    
    datos = [10, 15, 20, 5, 8, 25, 2, 12]
    print("Datos:", datos)
    print()
    
    # Detectar runs manualmente
    print("Secuencias naturales (runs):")
    print("1. [10, 15, 20]  (10->15->20: ascendente)")
    print("2. [5, 8, 25]    (5->8->25: ascendente)") 
    print("3. [2, 12]       (2->12: ascendente)")
    print()
    
    print("Distribucion en 2 archivos:")
    print("Archivo 1: [10,15,20], [2,12]")
    print("Archivo 2: [5,8,25]")
    print()
    
    print("Listo para fusion!")

# Ejecutar ejemplos
if __name__ == "__main__":
    ejemplo_completo()
    ejemplo_simple()