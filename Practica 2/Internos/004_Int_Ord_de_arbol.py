class NodoArbol:
    """Nodo para el arbol binario de busqueda"""
    
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def insertar_nodo(raiz, valor):
    """Inserta un nuevo valor en el arbol"""
    if raiz is None:
        return NodoArbol(valor)
    
    if valor < raiz.valor:
        raiz.izquierdo = insertar_nodo(raiz.izquierdo, valor)
    else:
        raiz.derecho = insertar_nodo(raiz.derecho, valor)
    
    return raiz

def inorden_traversal(raiz, resultado):
    """Recorrido inorden para obtener elementos ordenados"""
    if raiz is not None:
        inorden_traversal(raiz.izquierdo, resultado)
        resultado.append(raiz.valor)
        inorden_traversal(raiz.derecho, resultado)

def tree_sort(arr):
    """Ordenamiento usando arbol binario de busqueda"""
    if not arr:
        return arr
    
    # Construir el arbol
    raiz = None
    for valor in arr:
        raiz = insertar_nodo(raiz, valor)
    
    # Obtener elementos ordenados
    resultado = []
    inorden_traversal(raiz, resultado)
    return resultado

def mostrar_arbol(raiz, nivel=0, prefijo="Raiz: "):
    """Muestra el arbol de forma grafica simple"""
    if raiz is not None:
        print(" " * (nivel * 4) + prefijo + str(raiz.valor))
        if raiz.izquierdo is not None or raiz.derecho is not None:
            if raiz.izquierdo is not None:
                mostrar_arbol(raiz.izquierdo, nivel + 1, "Izq:  ")
            else:
                print(" " * ((nivel + 1) * 4) + "Izq:  None")
            if raiz.derecho is not None:
                mostrar_arbol(raiz.derecho, nivel + 1, "Der:  ")
            else:
                print(" " * ((nivel + 1) * 4) + "Der:  None")

def ejemplo_paso_a_paso(arr):
    """Muestra el proceso paso a paso"""
    print("PROCESO DE TREE SORT")
    print("====================")
    print(f"Array original: {arr}")
    
    # Construir arbol paso a paso
    raiz = None
    print("\nConstruyendo el arbol:")
    
    for i, valor in enumerate(arr):
        print(f"\nInsertando {valor}:")
        raiz = insertar_nodo(raiz, valor)
        mostrar_arbol(raiz)
        print("-" * 30)
    
    # Mostrar recorrido inorden
    print("\nRecorrido Inorden (ordenado):")
    resultado = []
    inorden_traversal(raiz, resultado)
    print(f"Resultado: {resultado}")
    
    return resultado

def prueba_simple():
    """Prueba simple del algoritmo"""
    print("PRUEBA SIMPLE DE TREE SORT")
    print("==========================")
    
    # Caso de prueba 1
    arr1 = [5, 2, 8, 1, 9]
    print(f"Array: {arr1}")
    resultado1 = tree_sort(arr1)
    print(f"Ordenado: {resultado1}")
    
    # Caso de prueba 2
    arr2 = [64, 34, 25, 12, 22]
    print(f"\nArray: {arr2}")
    resultado2 = tree_sort(arr2)
    print(f"Ordenado: {resultado2}")

def comparar_con_sorted():
    """Compara con la funcion sorted de Python"""
    print("\nCOMPARACION CON PYTHON SORTED")
    print("=============================")
    
    arr = [30, 10, 50, 20, 40]
    print(f"Array: {arr}")
    
    tree_result = tree_sort(arr)
    python_result = sorted(arr)
    
    print(f"Tree Sort: {tree_result}")
    print(f"Python sorted: {python_result}")
    print(f"Son iguales: {tree_result == python_result}")

def explicacion_teorica():
    """Explica como funciona el algoritmo"""
    print("\nCOMO FUNCIONA TREE SORT")
    print("======================")
    print("1. Se construye un arbol binario de busqueda")
    print("2. Los valores menores van a la izquierda")
    print("3. Los valores mayores o iguales van a la derecha")
    print("4. Se hace recorrido INORDEN para obtener ordenados")
    print("5. Complejidad: O(n log n) en promedio")
    print("6. Complejidad: O(n^2) en peor caso (arbol degenerado)")

# Programa principal
if __name__ == "__main__":
    # Ejemplo principal paso a paso
    numeros = [50, 30, 70, 20, 40, 60, 80]
    ejemplo_paso_a_paso(numeros)
    
    # Pruebas simples
    prueba_simple()
    
    # Comparacion
    comparar_con_sorted()
    
    # Explicacion
    explicacion_teorica()
    
    # Ejemplo adicional
    print("\nEJEMPLO ADICIONAL")
    print("=================")
    arr_extra = [3, 1, 4, 1, 5, 9, 2]
    print(f"Array con duplicados: {arr_extra}")
    resultado_extra = tree_sort(arr_extra)
    print(f"Ordenado: {resultado_extra}")