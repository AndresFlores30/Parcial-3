import heapq
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class MercadoDijkstraSimulator:
    def __init__(self, grafo):
        # Constructor: inicializa el simulador con un grafo de puestos del mercado
        self.grafo = grafo
        self.nodos = list(grafo.keys())
        
    def dijkstra_consola(self, inicio, producto_deseado):
        # Implementa el algoritmo de Dijkstra para buscar el mejor precio
        print("=" * 60)
        print("MERCADO - BUSCADOR DE MEJORES PRECIOS")
        print("=" * 60)
        print(f"Puesto inicial: {inicio}")
        print(f"Producto buscado: {producto_deseado}")
        print()
        
        # INICIALIZACIÓN DEL ALGORITMO
        # Precios infinitos para todos los puestos excepto el inicial
        precios = {nodo: float('inf') for nodo in self.nodos}
        precios[inicio] = 0  # El precio en el puesto inicial es 0 (punto de partida)
        
        predecesores = {nodo: None for nodo in self.nodos}
        visitados = set()
        cola = [(0, inicio)]
        
        paso = 1
        puesto_encontrado = None
        mejor_precio = float('inf')
        
        while cola:
            print(f"--- PASO DE BÚSQUEDA {paso} ---")
            print(f"Cola de prioridad (puestos a visitar): {cola}")
            print(f"Mejores precios encontrados: {precios}")
            print(f"Puestos visitados: {visitados}")
            print()
            
            precio_actual, puesto_actual = heapq.heappop(cola)
            
            if puesto_actual in visitados:
                print(f"  Puesto {puesto_actual} ya visitado, continuando...")
                print()
                continue
                
            print(f"Visitando puesto: {puesto_actual} (precio acumulado: ${precio_actual})")
            visitados.add(puesto_actual)
            
            # Verificar si este puesto tiene el producto deseado
            if producto_deseado in self.grafo[puesto_actual].get('productos', []):
                precio_total = precio_actual + self.grafo[puesto_actual]['productos'][producto_deseado]
                print(f"  ¡PRODUCTO ENCONTRADO en {puesto_actual}!")
                print(f"  Precio del producto: ${self.grafo[puesto_actual]['productos'][producto_deseado]}")
                print(f"  Precio total (incluyendo recorrido): ${precio_total}")
                
                if precio_total < mejor_precio:
                    mejor_precio = precio_total
                    puesto_encontrado = puesto_actual
                    print(f"  ✓ Este es el MEJOR PRECIO hasta ahora")
            
            # EXPLORAR PUESTOS VECINOS
            for conexion, distancia in self.grafo[puesto_actual]['conexiones']:
                if conexion in visitados:
                    continue
                    
                nuevo_precio = precio_actual + distancia
                print(f"  Conexión a: {conexion}, distancia: {distancia} metros")
                print(f"    Precio acumulado actual en {conexion}: ${precios[conexion]}")
                print(f"    Nuevo precio calculado: ${nuevo_precio}")
                
                if nuevo_precio < precios[conexion]:
                    precios[conexion] = nuevo_precio
                    predecesores[conexion] = puesto_actual
                    heapq.heappush(cola, (nuevo_precio, conexion))
                    print(f"    ✓ RUTA ACTUALIZADA: mejor camino encontrado")
                else:
                    print(f"    ✗ RUTA DESCARTADA: camino más largo")
                print()
            
            paso += 1
            print("-" * 40)
        
        # MOSTRAR RESULTADOS FINALES
        print("\n" + "=" * 60)
        print("RESULTADOS DE LA BÚSQUEDA")
        print("=" * 60)
        
        if puesto_encontrado:
            ruta = self._reconstruir_ruta(predecesores, inicio, puesto_encontrado)
            print(f"MEJOR OPCIÓN ENCONTRADA:")
            print(f"  Producto: {producto_deseado}")
            print(f"  Puesto: {puesto_encontrado}")
            print(f"  Precio del producto: ${self.grafo[puesto_encontrado]['productos'][producto_deseado]}")
            print(f"  Distancia recorrida: {precios[puesto_encontrado]} metros")
            print(f"  Precio total a pagar: ${mejor_precio}")
            print(f"  Ruta a seguir: {' → '.join(ruta)}")
            
            # Mostrar otras opciones encontradas
            print(f"\nOTRAS OPCIONES DISPONIBLES:")
            for puesto in self.nodos:
                if puesto != puesto_encontrado and producto_deseado in self.grafo[puesto].get('productos', []):
                    precio_producto = self.grafo[puesto]['productos'][producto_deseado]
                    print(f"  {puesto}: ${precio_producto} (a {precios[puesto] if precios[puesto] != float('inf') else '?'} metros)")
        else:
            print(f"No se encontró el producto '{producto_deseado}' en ningún puesto del mercado.")
            print("Sugerencia: Pruebe con otro producto o verifique la ortografía.")
        
        return precios, predecesores, puesto_encontrado, mejor_precio
    
    def _reconstruir_ruta(self, predecesores, inicio, destino):
        ruta = []
        actual = destino
        
        while actual is not None:
            ruta.append(actual)
            actual = predecesores[actual]
        
        ruta.reverse()
        return ruta if ruta and ruta[0] == inicio else [inicio, "Ruta no disponible"]
    
    def dijkstra_grafico(self, inicio, producto_deseado):
        print("\n" + "=" * 60)
        print("MERCADO - MAPA DE PRECIOS Y RUTAS")
        print("=" * 60)
        
        precios, predecesores, puesto_optimo, mejor_precio = self.dijkstra_consola(inicio, producto_deseado)
        
        # CONFIGURACIÓN DE LA VISUALIZACIÓN
        plt.figure(figsize=(14, 10))
        G = nx.Graph()
        
        # CONSTRUIR EL GRAFO VISUAL
        for nodo in self.grafo:
            G.add_node(nodo, productos=list(self.grafo[nodo].get('productos', {}).keys()))
            for conexion, distancia in self.grafo[nodo]['conexiones']:
                G.add_edge(nodo, conexion, weight=distancia)
        
        pos = nx.spring_layout(G, seed=42, k=3, iterations=50)
        
        # IDENTIFICAR TIPOS DE NODOS
        puestos_con_producto = []
        puestos_sin_producto = []
        
        for nodo in self.nodos:
            if producto_deseado in self.grafo[nodo].get('productos', []):
                puestos_con_producto.append(nodo)
            else:
                puestos_sin_producto.append(nodo)
        
        # DIBUJAR PUESTOS SIN EL PRODUCTO (gris)
        nx.draw_networkx_nodes(G, pos, nodelist=puestos_sin_producto, 
                              node_size=700, node_color='#CCCCCC', 
                              alpha=0.7, edgecolors='#666666', linewidths=1)
        
        # DIBUJAR PUESTOS CON EL PRODUCTO (azul claro)
        nx.draw_networkx_nodes(G, pos, nodelist=puestos_con_producto, 
                              node_size=800, node_color='#87CEEB', 
                              alpha=0.8, edgecolors='#0000FF', linewidths=2)
        
        # DESTACAR EL PUESTO CON MEJOR PRECIO (verde)
        if puesto_optimo:
            nx.draw_networkx_nodes(G, pos, nodelist=[puesto_optimo], 
                                  node_size=900, node_color='#90EE90', 
                                  alpha=0.9, edgecolors='#006400', linewidths=3)
        
        # DESTACAR EL PUESTO INICIAL (amarillo)
        nx.draw_networkx_nodes(G, pos, nodelist=[inicio], 
                              node_size=800, node_color='#FFD700', 
                              alpha=0.8, edgecolors='#FF8C00', linewidths=2)
        
        # DIBUJAR ARISTAS
        nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color='#888888', 
                              width=2, style='solid')
        
        # ETIQUETAS DE NODOS
        labels = {}
        for nodo in self.nodos:
            if producto_deseado in self.grafo[nodo].get('productos', []):
                precio = self.grafo[nodo]['productos'][producto_deseado]
                labels[nodo] = f"{nodo}\n${precio}"
            else:
                labels[nodo] = nodo
        
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=9, 
                               font_weight='bold', font_family='sans-serif',
                               bbox=dict(boxstyle="round,pad=0.3", 
                                       facecolor='white', 
                                       edgecolor='black',
                                       alpha=0.9))
        
        # ETIQUETAS DE DISTANCIAS
        edge_labels = {(u, v): f"{d['weight']}m" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                   font_color='#333333', font_size=8)
        
        # RESALTAR RUTA ÓPTIMA AL PUESTO CON MEJOR PRECIO
        if puesto_optimo:
            ruta_optima = self._reconstruir_ruta(predecesores, inicio, puesto_optimo)
            if len(ruta_optima) > 1 and ruta_optima[-1] == puesto_optimo:
                edges_ruta = [(ruta_optima[i], ruta_optima[i+1]) for i in range(len(ruta_optima)-1)]
                nx.draw_networkx_edges(G, pos, edgelist=edges_ruta, 
                                     width=4, alpha=0.8, edge_color='#32CD32')
        
        # CONFIGURACIÓN FINAL
        titulo = f"MERCADO - Búsqueda de '{producto_deseado}'\n"
        titulo += f"Desde: {inicio}"
        if puesto_optimo:
            titulo += f" | Mejor opción: {puesto_optimo} (${mejor_precio})"
        
        plt.title(titulo, fontsize=14, fontweight='bold', pad=20)
        
        # LEYENDA
        leyenda = [
            "Puesto inicial",
            "Puesto con producto",
            "Mejor precio encontrado",
            "Puesto sin producto",
            "--- Distancias en metros"
        ]
        
        colores = ['#FFD700', '#87CEEB', '#90EE90', '#CCCCCC']
        y_pos = 0.02
        for i, texto in enumerate(leyenda[:-1]):
            plt.figtext(0.02, 0.05 + i*0.03, f"● {texto}", 
                       color=colores[i], fontsize=9,
                       bbox=dict(boxstyle="round", facecolor='white', 
                               edgecolor='gray', alpha=0.8))
        
        plt.figtext(0.02, 0.02, leyenda[-1], color='#666666', fontsize=8,
                   bbox=dict(boxstyle="round", facecolor='white', 
                           edgecolor='gray', alpha=0.8))
        
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
        return precios, predecesores, puesto_optimo, mejor_precio

def crear_mercado():
    """Crea la estructura del mercado con puestos, productos y distancias"""
    mercado = {
        'ENTRADA': {
            'conexiones': [('PUESTO1', 10), ('PUESTO2', 15), ('INFO', 5)],
            'productos': {}
        },
        'INFO': {
            'conexiones': [('ENTRADA', 5), ('PUESTO3', 8), ('PUESTO4', 12)],
            'productos': {'mapas': 2}  # Puesto de información
        },
        'PUESTO1': {
            'conexiones': [('ENTRADA', 10), ('PUESTO5', 7), ('PUESTO6', 9)],
            'productos': {'manzanas': 3, 'peras': 4, 'naranjas': 5}
        },
        'PUESTO2': {
            'conexiones': [('ENTRADA', 15), ('PUESTO7', 6), ('PUESTO8', 8)],
            'productos': {'tomates': 4, 'cebollas': 3, 'zanahorias': 2}
        },
        'PUESTO3': {
            'conexiones': [('INFO', 8), ('PUESTO9', 5), ('PUESTO10', 7)],
            'productos': {'papas': 2, 'batatas': 3, 'mandioca': 4}
        },
        'PUESTO4': {
            'conexiones': [('INFO', 12), ('PUESTO11', 4), ('PUESTO12', 6)],
            'productos': {'fresas': 8, 'arandanos': 10, 'frambuesas': 9}
        },
        'PUESTO5': {
            'conexiones': [('PUESTO1', 7), ('PUESTO13', 8)],
            'productos': {'manzanas': 2, 'peras': 3}  # Mejor precio en manzanas
        },
        'PUESTO6': {
            'conexiones': [('PUESTO1', 9), ('PUESTO14', 5)],
            'productos': {'naranjas': 4, 'limones': 3}
        },
        'PUESTO7': {
            'conexiones': [('PUESTO2', 6), ('PUESTO15', 7)],
            'productos': {'tomates': 3, 'cebollas': 2}  # Mejor precio en tomates
        },
        'PUESTO8': {
            'conexiones': [('PUESTO2', 8), ('PUESTO16', 9)],
            'productos': {'zanahorias': 1, 'remolachas': 3}  # Mejor precio en zanahorias
        },
        'PUESTO9': {
            'conexiones': [('PUESTO3', 5), ('PUESTO17', 6)],
            'productos': {'papas': 1, 'batatas': 2}  # Mejor precio en papas
        },
        'PUESTO10': {
            'conexiones': [('PUESTO3', 7), ('PUESTO18', 8)],
            'productos': {'lechuga': 3, 'espinaca': 4}
        },
        'PUESTO11': {
            'conexiones': [('PUESTO4', 4), ('PUESTO19', 5)],
            'productos': {'fresas': 7, 'frutillas': 6}
        },
        'PUESTO12': {
            'conexiones': [('PUESTO4', 6), ('PUESTO20', 7)],
            'productos': {'arandanos': 9, 'frambuesas': 8}
        },
        'PUESTO13': {
            'conexiones': [('PUESTO5', 8)],
            'productos': {'bananas': 4, 'mangos': 6}
        },
        'PUESTO14': {
            'conexiones': [('PUESTO6', 5)],
            'productos': {'limones': 2, 'pomelos': 4}
        },
        'PUESTO15': {
            'conexiones': [('PUESTO7', 7)],
            'productos': {'ajo': 5, 'perejil': 2}
        },
        'PUESTO16': {
            'conexiones': [('PUESTO8', 9)],
            'productos': {'remolachas': 2, 'nabos': 3}
        },
        'PUESTO17': {
            'conexiones': [('PUESTO9', 6)],
            'productos': {'cebollas': 2, 'puerros': 4}
        },
        'PUESTO18': {
            'conexiones': [('PUESTO10', 8)],
            'productos': {'espinaca': 3, 'acelga': 3}
        },
        'PUESTO19': {
            'conexiones': [('PUESTO11', 5)],
            'productos': {'frutillas': 5, 'cerezas': 7}
        },
        'PUESTO20': {
            'conexiones': [('PUESTO12', 7)],
            'productos': {'frambuesas': 7, 'moras': 6}
        }
    }
    return mercado

def main():
    mercado = crear_mercado()
    simulador = MercadoDijkstraSimulator(mercado)
    
    # Lista de productos disponibles
    todos_productos = set()
    for puesto in mercado.values():
        todos_productos.update(puesto['productos'].keys())
    productos_ordenados = sorted(list(todos_productos))
    
    while True:
        print("\n" + "=" * 60)
        print("MERCADO - BUSCADOR DE PRECIOS")
        print("=" * 60)
        print("1. Buscar mejor precio de un producto")
        print("2. Ver mapa del mercado")
        print("3. Ver todos los productos disponibles")
        print("4. Salir")
        
        opcion = input("\nSeleccione opcion (1-4): ").strip()
        
        if opcion == '1':
            print(f"\nPuestos disponibles: {sorted(list(mercado.keys()))}")
            inicio = input("Ingrese puesto de entrada: ").strip().upper()
            
            if inicio in mercado:
                print(f"\nProductos disponibles: {productos_ordenados}")
                producto = input("Ingrese producto a buscar: ").strip().lower()
                
                # Buscar producto en cualquier forma (case-insensitive)
                producto_encontrado = None
                for p in productos_ordenados:
                    if p.lower() == producto:
                        producto_encontrado = p
                        break
                
                if producto_encontrado:
                    print(f"\nModo de búsqueda:")
                    print("1. Solo consola (texto)")
                    print("2. Con mapa visual")
                    
                    modo = input("Seleccione modo (1-2): ").strip()
                    
                    if modo == '1':
                        simulador.dijkstra_consola(inicio, producto_encontrado)
                    elif modo == '2':
                        simulador.dijkstra_grafico(inicio, producto_encontrado)
                    else:
                        print("Opcion no valida")
                else:
                    print(f"Producto '{producto}' no encontrado")
            else:
                print("Puesto no valido")
                
        elif opcion == '2':
            # Mostrar mapa general sin búsqueda específica
            plt.figure(figsize=(14, 10))
            G = nx.Graph()
            
            for nodo in mercado:
                G.add_node(nodo)
                for conexion, distancia in mercado[nodo]['conexiones']:
                    G.add_edge(nodo, conexion, weight=distancia)
            
            pos = nx.spring_layout(G, seed=42, k=3, iterations=50)
            
            nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', alpha=0.7)
            nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color='gray')
            nx.draw_networkx_labels(G, pos, font_size=8)
            
            edge_labels = {(u, v): f"{d['weight']}m" for u, v, d in G.edges(data=True)}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)
            
            plt.title("Mapa del Mercado - Distribución de Puestos", fontsize=14, fontweight='bold')
            plt.axis('off')
            plt.tight_layout()
            plt.show()
            
        elif opcion == '3':
            print("\nPRODUCTOS DISPONIBLES POR CATEGORÍA:")
            
            frutas = ['manzanas', 'peras', 'naranjas', 'fresas', 'arandanos', 'frambuesas', 
                     'bananas', 'mangos', 'limones', 'pomelos', 'frutillas', 'cerezas', 'moras']
            verduras = ['tomates', 'cebollas', 'zanahorias', 'papas', 'batatas', 'mandioca',
                       'lechuga', 'espinaca', 'ajo', 'perejil', 'puerros', 'acelga', 'nabos',
                       'remolachas']
            
            print("\nFRUTAS:")
            for fruta in sorted([f for f in productos_ordenados if f in frutas]):
                print(f"  • {fruta.capitalize()}")
            
            print("\nVERDURAS Y HORTALIZAS:")
            for verdura in sorted([v for v in productos_ordenados if v in verduras]):
                print(f"  • {verdura.capitalize()}")
            
            print("\nOTROS:")
            otros = [p for p in productos_ordenados if p not in frutas and p not in verduras]
            for otro in sorted(otros):
                print(f"  • {otro.capitalize()}")
                
        elif opcion == '4':
            print("Gracias por usar el buscador de precios del mercado. ¡Hasta pronto!")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()