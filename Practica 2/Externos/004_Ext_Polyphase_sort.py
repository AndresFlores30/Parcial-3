def polyphase_muy_simple(arr):
    """
    Polyphase Sort
    """
    if len(arr) <= 1:
        return arr
    
    print("Datos originales:", arr)
    print()
    
    # Crear 3 listas
    lista1 = []
    lista2 = []
    lista3 = []  # Esta empieza vacia
    
    # Repartir los datos en 2 listas
    for i, num in enumerate(arr):
        if i % 2 == 0:
            lista1.append(num)
        else:
            lista2.append(num)
    
    print("Despues de repartir:")
    print("Lista 1:", lista1)
    print("Lista 2:", lista2) 
    print("Lista 3:", lista3, "(vacia)")
    print()
    
    # Ordenar las listas
    lista1.sort()
    lista2.sort()
    
    print("Despues de ordenar:")
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista 3:", lista3)
    print()
    
    paso = 1
    # Fusionar hasta que todo este en una lista
    while lista1 and lista2:
        print(f"Paso {paso}:")
        
        # Comparar primeros elementos
        if lista1[0] < lista2[0]:
            mover = lista1.pop(0)
            print(f"  {lista1[0] if lista1 else 'Nada'} < {lista2[0] if lista2 else 'Nada'}")
            print(f"  Mover {mover} de Lista 1 a Lista 3")
            lista3.append(mover)
        else:
            mover = lista2.pop(0)
            print(f"  {lista1[0] if lista1 else 'Nada'} > {lista2[0] if lista2 else 'Nada'}")
            print(f"  Mover {mover} de Lista 2 a Lista 3")
            lista3.append(mover)
        
        # Ordenar lista3
        lista3.sort()
        
        print(f"  Lista 1: {lista1}")
        print(f"  Lista 2: {lista2}")
        print(f"  Lista 3: {lista3}")
        print()
        paso += 1
    
    # Agregar lo que quede
    if lista1:
        lista3.extend(lista1)
        print(f"Agregar resto de Lista 1: {lista1}")
    if lista2:
        lista3.extend(lista2)
        print(f"Agregar resto de Lista 2: {lista2}")
    
    print("\nResultado final:", lista3)
    return lista3

# Ejemplos de uso
print("=== EJEMPLO 1 ===")
datos1 = [25, 10, 35, 5]
resultado1 = polyphase_muy_simple(datos1)

print("\n" + "="*50)
print("=== EJEMPLO 2 ===")
datos2 = [8, 3, 1, 7, 4]
resultado2 = polyphase_muy_simple(datos2)

print("\n" + "="*50)
print("=== EJEMPLO 3 ===")
datos3 = [15, 2]
resultado3 = polyphase_muy_simple(datos3)