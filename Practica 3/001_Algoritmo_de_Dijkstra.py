import heapq
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class CineDijkstraSimulator:
    def __init__(self, grafo):
        # Constructor: inicializa el simulador con un grafo dado
        self.grafo = grafo  # Almacena la estructura del sistema (nodos y conexiones)
        self.nodos = list(grafo.keys())  # Lista de todos los nodos del sistema
        
    def dijkstra_consola(self, inicio, destino_cine):
        # Implementa el algoritmo de Dijkstra mostrando paso a paso en consola
        print("=" * 60)
        print("CINE - SIMULADOR DE RUTAS AL CINE")
        print("=" * 60)
        print(f"Punto de partida: {inicio}")
        print(f"Destino (Cine): {destino_cine}")
        print()
        
        # INICIALIZACIÓN DEL ALGORITMO
        # Distancias infinitas para todos los nodos excepto el inicial
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[inicio] = 0  # La distancia al nodo inicial es 0
        
        predecesores = {nodo: None for nodo in self.nodos}  # Para reconstruir rutas
        visitados = set()  # Conjunto de nodos ya procesados
        cola = [(0, inicio)]  # Cola de prioridad (min-heap) con (distancia, nodo)
        
        paso = 1  # Contador de pasos para mostrar progreso
        
        # BUCLE PRINCIPAL DEL ALGORITMO
        while cola:
            # Mostrar estado actual del algoritmo
            print(f"--- CICLO DE PROCESAMIENTO {paso} ---")
            print(f"Cola de prioridad: {cola}")
            print(f"Distancias actuales: {distancias}")
            print(f"Nodos procesados: {visitados}")
            print()
            
            # Extraer el nodo con menor distancia de la cola de prioridad
            distancia_actual, nodo_actual = heapq.heappop(cola)
            
            # Si el nodo ya fue visitado, saltar a la siguiente iteración
            if nodo_actual in visitados:
                print(f"  Nodo {nodo_actual} ya procesado, continuando...")
                print()
                continue
            
            # Verificar si llegamos al cine
            if nodo_actual == destino_cine:
                print(f"¡LLEGAMOS AL CINE! Nodo: {nodo_actual}")
                print(f"Distancia total recorrida: {distancia_actual} minutos")
                break
                
            # Procesar el nodo actual
            print(f"Procesando nodo: {nodo_actual} (distancia recorrida: {distancia_actual} min)")
            visitados.add(nodo_actual)  # Marcar como visitado
            
            # EXPLORAR VECINOS DEL NODO ACTUAL
            for conexion, tiempo in self.grafo[nodo_actual]:
                # Saltar vecinos ya visitados
                if conexion in visitados:
                    continue
                    
                # Calcular nueva distancia tentativa
                nueva_distancia = distancia_actual + tiempo
                print(f"  Conexion encontrada: {conexion}, tiempo de viaje: {tiempo} min")
                print(f"  Tiempo actual a {conexion}: {distancias[conexion]} min")
                print(f"  Nuevo tiempo calculado: {nueva_distancia} min")
                
                # ACTUALIZAR DISTANCIAS SI ENCONTRAMOS UN CAMINO MÁS CORTO
                if nueva_distancia < distancias[conexion]:
                    distancias[conexion] = nueva_distancia
                    predecesores[conexion] = nodo_actual
                    heapq.heappush(cola, (nueva_distancia, conexion))
                    print(f"  RUTA ACTUALIZADA: {conexion} = {nueva_distancia} min")
                else:
                    print(f"  MANTENIENDO RUTA ACTUAL (más larga o igual)")
                print()
            
            paso += 1
            print("-" * 40)
        
        # MOSTRAR RESULTADOS FINALES
        print("\n" + "=" * 60)
        print("RESULTADO FINAL - RUTA AL CINE")
        print("=" * 60)
        
        # Reconstruir y mostrar la ruta óptima al cine
        ruta_cine = self._reconstruir_ruta(predecesores, inicio, destino_cine)
        if ruta_cine[0] == inicio and destino_cine in ruta_cine:
            print(f"Ruta más corta al cine '{destino_cine}':")
            print(f"  Recorrido: {' → '.join(ruta_cine)}")
            print(f"  Tiempo total: {distancias[destino_cine]} minutos")
            print(f"  Número de paradas: {len(ruta_cine)-1}")
        else:
            print(f"No se encontró una ruta desde {inicio} hasta el cine {destino_cine}")
        
        return distancias, predecesores
    
    def _reconstruir_ruta(self, predecesores, inicio, destino):
        # Reconstruye la ruta óptima desde el inicio hasta el destino
        ruta = []
        actual = destino
        
        # Seguir la cadena de predecesores desde el destino hasta el inicio
        while actual is not None:
            ruta.append(actual)
            actual = predecesores[actual]
        
        ruta.reverse()  # Invertir para tener la ruta en orden correcto
        
        # Verificar que la ruta comienza en el nodo inicial
        return ruta if ruta and ruta[0] == inicio else [inicio, "Ruta no disponible"]
    
    def dijkstra_grafico(self, inicio, destino_cine):
        # Versión gráfica del algoritmo con visualización
        print("\n" + "=" * 60)
        print("CINE - VISUALIZACIÓN DE RUTAS")
        print("=" * 60)
        
        # Ejecutar Dijkstra para obtener distancias y predecesores
        distancias, predecesores = self.dijkstra_consola(inicio, destino_cine)
        
        # CONFIGURACIÓN DE LA VISUALIZACIÓN
        plt.figure(figsize=(14, 10))
        G = nx.Graph()  # Crear grafo de NetworkX
        
        # Estilo visual cine (fondo oscuro)
        plt.style.use('dark_background')
        fig = plt.gcf()
        fig.patch.set_facecolor('#1a1a1a')
        
        # CONSTRUIR EL GRAFO VISUAL
        # Agregar nodos y aristas al grafo de NetworkX
        for nodo in self.grafo:
            G.add_node(nodo)
            for conexion, tiempo in self.grafo[nodo]:
                G.add_edge(nodo, conexion, weight=tiempo)
        
        # Calcular posiciones de los nodos para el diseño
        pos = nx.spring_layout(G, seed=42, k=2, iterations=50)
        
        # DIBUJAR ELEMENTOS DEL GRAFO
        
        # Nodos regulares: color amarillo suave
        nodos_regulares = [n for n in self.nodos if n != destino_cine]
        nx.draw_networkx_nodes(G, pos, nodelist=nodos_regulares, 
                              node_size=800, node_color='#FFD700', 
                              alpha=0.8, edgecolors='#FFFFFF', linewidths=2)
        
        # Nodo del cine: color rojo brillante (destacado)
        nx.draw_networkx_nodes(G, pos, nodelist=[destino_cine], 
                              node_size=1000, node_color='#FF4444', 
                              alpha=0.9, edgecolors='#FFFFFF', linewidths=3)
        
        # Aristas: color azul claro
        nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color='#87CEEB', 
                              width=2, style='solid')
        
        # Etiquetas de nodos
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', 
                               font_family='sans-serif',
                               bbox=dict(boxstyle="round,pad=0.3", 
                                       facecolor='#333333', 
                                       edgecolor='#FFD700',
                                       alpha=0.8))
        
        # Etiquetas de pesos en las aristas (tiempo en minutos)
        edge_labels = {(u, v): f"{d['weight']} min" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                   font_color='#FFFFFF',
                                   font_size=8,
                                   bbox=dict(boxstyle="round", 
                                           facecolor='#444444', 
                                           edgecolor='#87CEEB',
                                           alpha=0.8))
        
        # RESALTAR RUTA ÓPTIMA AL CINE
        ruta_cine = self._reconstruir_ruta(predecesores, inicio, destino_cine)
        if len(ruta_cine) > 1 and ruta_cine[-1] == destino_cine:
            # Crear lista de aristas que forman la ruta óptima
            edges_ruta = [(ruta_cine[i], ruta_cine[i+1]) for i in range(len(ruta_cine)-1)]
            
            # Dibujar ruta óptima en verde brillante
            nx.draw_networkx_edges(G, pos, edgelist=edges_ruta, 
                                 width=4, alpha=0.9, edge_color='#32CD32')
            
            # Resaltar nodos de la ruta
            nx.draw_networkx_nodes(G, pos, nodelist=ruta_cine, 
                                 node_size=900, node_color='#32CD32', alpha=0.7)
        
        # CONFIGURACIÓN FINAL DEL GRÁFICO
        tiempo_total = distancias[destino_cine] if destino_cine in distancias else "?"
        titulo = f"RUTA AL CINE\n{inicio} → {destino_cine} | Tiempo: {tiempo_total} minutos"
        plt.title(titulo, fontsize=16, fontweight='bold', color='#FFD700', 
                 fontfamily='sans-serif', pad=20)
        
        # Añadir leyenda explicativa
        leyenda = "● Nodos: Intersecciones\n★ CINE: Destino final\n🟢 Verde: Ruta más corta\n--- Tiempos en minutos"
        plt.figtext(0.02, 0.02, leyenda, fontsize=10, color='#FFFFFF',
                   bbox=dict(boxstyle="round", facecolor='#222222', 
                           edgecolor='#FFD700', alpha=0.9))
        
        plt.axis('off')  # Ocultar ejes
        plt.tight_layout()
        plt.show()
        
        return distancias, predecesores

# Grafo de la ciudad con cines
def crear_mapa_ciudad():
    # Define la topología de la ciudad con nombres de lugares
    # Los valores representan minutos de viaje entre ubicaciones
    mapa_ciudad = {
        'PLAZA_CENTRAL': [('MERCADO', 5), ('ESTACION_TREN', 8), ('PARQUE', 3)],
        'MERCADO': [('PLAZA_CENTRAL', 5), ('BIBLIOTECA', 4), ('CINE_ALPHA', 7)],
        'ESTACION_TREN': [('PLAZA_CENTRAL', 8), ('UNIVERSIDAD', 6), ('CINE_BETA', 10)],
        'PARQUE': [('PLAZA_CENTRAL', 3), ('BIBLIOTECA', 2), ('ESTADIO', 5)],
        'BIBLIOTECA': [('MERCADO', 4), ('PARQUE', 2), ('UNIVERSIDAD', 3)],
        'UNIVERSIDAD': [('ESTACION_TREN', 6), ('BIBLIOTECA', 3), ('CINE_BETA', 4)],
        'ESTADIO': [('PARQUE', 5), ('CINE_ALPHA', 6), ('CINE_BETA', 7)],
        'CINE_ALPHA': [('MERCADO', 7), ('ESTADIO', 6)],  # Cine 1
        'CINE_BETA': [('ESTACION_TREN', 10), ('UNIVERSIDAD', 4), ('ESTADIO', 7)]  # Cine 2
    }
    return mapa_ciudad

def main():
    # Función principal que maneja la interfaz de usuario
    # Crear mapa de la ciudad
    mapa_ciudad = crear_mapa_ciudad()
    
    # Lista de cines disponibles
    cines_disponibles = ['CINE_ALPHA', 'CINE_BETA']
    
    # Inicializar simulador
    simulador = CineDijkstraSimulator(mapa_ciudad)
    
    # BUCLE PRINCIPAL DE LA INTERFAZ
    while True:
        print("\n" + "=" * 60)
        print("SISTEMA DE RUTAS AL CINE")
        print("=" * 60)
        print("1. Buscar ruta al cine (modo consola)")
        print("2. Visualizar mapa y ruta al cine")
        print("3. Salir del sistema")
        
        opcion = input("\nSeleccione opcion (1-3): ").strip()
        
        # OPCIÓN 1: Modo consola (solo texto)
        if opcion == '1':
            print("\nUbicaciones disponibles:", list(mapa_ciudad.keys()))
            print("Cines disponibles:", cines_disponibles)
            
            inicio = input("Ingrese punto de partida: ").strip().upper()
            if inicio in mapa_ciudad:
                print("\nCines disponibles:")
                for i, cine in enumerate(cines_disponibles, 1):
                    print(f"  {i}. {cine}")
                
                cine_opcion = input("Ingrese nombre del cine destino: ").strip().upper()
                if cine_opcion in mapa_ciudad:
                    simulador.dijkstra_consola(inicio, cine_opcion)
                else:
                    print("Cine no válido")
            else:
                print("Ubicación no válida")
                
        # OPCIÓN 2: Modo gráfico con visualización
        elif opcion == '2':
            print("\nUbicaciones disponibles:", list(mapa_ciudad.keys()))
            print("Cines disponibles:", cines_disponibles)
            
            inicio = input("Ingrese punto de partida: ").strip().upper()
            if inicio in mapa_ciudad:
                print("\nCines disponibles:")
                for i, cine in enumerate(cines_disponibles, 1):
                    print(f"  {i}. {cine}")
                
                cine_opcion = input("Ingrese nombre del cine destino: ").strip().upper()
                if cine_opcion in mapa_ciudad:
                    simulador.dijkstra_grafico(inicio, cine_opcion)
                else:
                    print("Cine no válido")
            else:
                print("Ubicación no válida")
                
        # OPCIÓN 3: Salir del programa
        elif opcion == '3':
            print("Disfrute su película")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    # Punto de entrada del programa
    main()