import heapq
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class TronDijkstraSimulator:
    def __init__(self, grafo):
        # Constructor: inicializa el simulador con un grafo dado
        self.grafo = grafo  # Almacena la estructura del sistema (nodos y conexiones)
        self.nodos = list(grafo.keys())  # Lista de todos los nodos del sistema
        
    def dijkstra_consola(self, inicio):
        # Implementa el algoritmo de Dijkstra mostrando paso a paso en consola
        print("=" * 60)
        print("TRON - SIMULADOR DE RUTAS OPTIMAS")
        print("=" * 60)
        print(f"Light Cycle inicial: {inicio}")
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
            print(f"Cola de prioridad del sistema: {cola}")
            print(f"Energia actual en nodos: {distancias}")
            print(f"Nodos procesados: {visitados}")
            print()
            
            # Extraer el nodo con menor distancia de la cola de prioridad
            energia_actual, nodo_actual = heapq.heappop(cola)
            
            # Si el nodo ya fue visitado, saltar a la siguiente iteración
            if nodo_actual in visitados:
                print(f"  Nodo {nodo_actual} ya procesado, continuando...")
                print()
                continue
                
            # Procesar el nodo actual
            print(f"Procesando nodo: {nodo_actual} (energia consumida: {energia_actual})")
            visitados.add(nodo_actual)  # Marcar como visitado
            
            # EXPLORAR VECINOS DEL NODO ACTUAL
            for conexion, consumo in self.grafo[nodo_actual]:
                # Saltar vecinos ya visitados
                if conexion in visitados:
                    continue
                    
                # Calcular nueva distancia tentativa
                nueva_energia = energia_actual + consumo
                print(f"  Conexion detectada: {conexion}, consumo de energia: {consumo}")
                print(f"  Energia actual en {conexion}: {distancias[conexion]}")
                print(f"  Nueva energia calculada: {nueva_energia}")
                
                # ACTUALIZAR DISTANCIAS SI ENCONTRAMOS UN CAMINO MÁS CORTO
                if nueva_energia < distancias[conexion]:
                    distancias[conexion] = nueva_energia
                    predecesores[conexion] = nodo_actual
                    heapq.heappush(cola, (nueva_energia, conexion))
                    print(f"  SISTEMA ACTUALIZADO: {conexion} = {nueva_energia}")
                else:
                    print(f"  MANTENIENDO CONFIGURACION ACTUAL")
                print()
            
            paso += 1
            print("-" * 40)
        
        # MOSTRAR RESULTADOS FINALES
        print("\n" + "=" * 60)
        print("ANALISIS FINAL DEL SISTEMA TRON")
        print("=" * 60)
        for nodo in self.nodos:
            # Reconstruir y mostrar la ruta óptima para cada nodo
            ruta = self._reconstruir_ruta(predecesores, inicio, nodo)
            print(f"Nodo {nodo}: Energia = {distancias[nodo]}, Ruta = {ruta}")
        
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
        return ruta if ruta[0] == inicio else "Ruta no disponible"
    
    def dijkstra_grafico(self, inicio, destino=None):
        # Versión gráfica del algoritmo con visualización estilo Tron
        print("\n" + "=" * 60)
        print("TRON - VISUALIZACION DEL SISTEMA")
        print("=" * 60)
        
        # Ejecutar Dijkstra para obtener distancias y predecesores
        distancias, predecesores = self.dijkstra_consola(inicio)
        
        # CONFIGURACIÓN DE LA VISUALIZACIÓN
        plt.figure(figsize=(14, 10))
        G = nx.Graph()  # Crear grafo de NetworkX
        
        # Estilo visual Tron (fondo negro)
        plt.style.use('dark_background')
        fig = plt.gcf()
        fig.patch.set_facecolor('black')
        
        # CONSTRUIR EL GRAFO VISUAL
        # Agregar nodos y aristas al grafo de NetworkX
        for nodo in self.grafo:
            G.add_node(nodo)
            for conexion, consumo in self.grafo[nodo]:
                G.add_edge(nodo, conexion, weight=consumo)
        
        # Calcular posiciones de los nodos para el diseño
        pos = nx.spring_layout(G, seed=42)  # seed para reproducibilidad
        
        # DIBUJAR ELEMENTOS DEL GRAFO
        
        # Nodos: cian con bordes blancos
        nx.draw_networkx_nodes(G, pos, node_size=800, 
                              node_color='#00FFFF', alpha=0.8,
                              edgecolors='#FFFFFF', linewidths=2)
        
        # Aristas: verde neón con estilo discontinuo
        nx.draw_networkx_edges(G, pos, alpha=0.6, 
                              edge_color='#00FF00', width=2,
                              style='dashed')
        
        # Etiquetas de nodos: estilo caja azul con texto en monoespaciado
        nx.draw_networkx_labels(G, pos, font_size=10, 
                               font_weight='bold', 
                               font_family='monospace',
                               bbox=dict(boxstyle="round,pad=0.3", 
                                       facecolor='#003366', 
                                       edgecolor='#00FFFF',
                                       alpha=0.8))
        
        # Etiquetas de pesos en las aristas
        edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                   font_color='#FFFF00',
                                   font_size=8,
                                   bbox=dict(boxstyle="round", 
                                           facecolor='black', 
                                           edgecolor='#FFFF00',
                                           alpha=0.8))
        
        # RESALTAR RUTA ÓPTIMA SI SE ESPECIFICA DESTINO
        if destino:
            ruta = self._reconstruir_ruta(predecesores, inicio, destino)
            if len(ruta) > 1:
                # Crear lista de aristas que forman la ruta óptima
                edges_ruta = [(ruta[i], ruta[i+1]) for i in range(len(ruta)-1)]
                
                # Dibujar ruta óptima en magenta
                nx.draw_networkx_edges(G, pos, edgelist=edges_ruta, 
                                     width=4, alpha=0.9, edge_color='#FF00FF')
                nx.draw_networkx_nodes(G, pos, nodelist=ruta, 
                                     node_size=1000, node_color='#FF00FF')
        
        # CONFIGURACIÓN FINAL DEL GRÁFICO
        plt.title(f"SISTEMA TRON - Light Cycle: {inicio}\nRuta de Minima Energia", 
                 fontsize=16, fontweight='bold', color='#00FFFF', 
                 fontfamily='monospace', pad=20)
        
        # Añadir leyenda explicativa
        legend_text = "Nodos: Estaciones de Energia\nLineas: Conexiones del Sistema\nMagenta: Ruta Optima"
        plt.figtext(0.02, 0.02, legend_text, fontsize=10, color='#00FF00',
                   bbox=dict(boxstyle="round", facecolor='#002244', 
                           edgecolor='#00FFFF', alpha=0.8))
        
        plt.axis('off')  # Ocultar ejes
        plt.tight_layout()
        plt.show()
        
        return distancias, predecesores

# Grafo temático de Tron
def crear_sistema_tron():
    # Define la topología del sistema Tron con nombres temáticos
    # Estructura: nodo: [(vecino, peso), (vecino, peso), ...]
    sistema_tron = {
        'CPU_CENTRAL': [('SECTOR_ALPHA', 4), ('RED_PRINCIPAL', 2)],
        'SECTOR_ALPHA': [('CPU_CENTRAL', 4), ('RED_PRINCIPAL', 1), ('TORRE_BETA', 5)],
        'RED_PRINCIPAL': [('CPU_CENTRAL', 2), ('SECTOR_ALPHA', 1), ('TORRE_BETA', 8), ('NODO_GAMMA', 10)],
        'TORRE_BETA': [('SECTOR_ALPHA', 5), ('RED_PRINCIPAL', 8), ('NODO_GAMMA', 2), ('TERMINAL_OMEGA', 6)],
        'NODO_GAMMA': [('RED_PRINCIPAL', 10), ('TORRE_BETA', 2), ('TERMINAL_OMEGA', 3)],
        'TERMINAL_OMEGA': [('TORRE_BETA', 6), ('NODO_GAMMA', 3)]
    }
    return sistema_tron

def main():
    # Función principal que maneja la interfaz de usuario
    # Crear sistema Tron con la topología definida
    sistema_tron = crear_sistema_tron()
    
    # Inicializar simulador
    simulador = TronDijkstraSimulator(sistema_tron)
    
    # BUCLE PRINCIPAL DE LA INTERFAZ
    while True:
        print("\n" + "=" * 60)
        print("SISTEMA DE NAVEGACION TRON")
        print("=" * 60)
        print("1. Ejecutar analisis de ruta (modo consola)")
        print("2. Visualizar sistema de energia")
        print("3. Salir del sistema")
        
        opcion = input("\nSeleccione opcion (1-3): ").strip()
        
        # OPCIÓN 1: Modo consola (solo texto)
        if opcion == '1':
            print("\nEstaciones disponibles:", list(sistema_tron.keys()))
            inicio = input("Ingrese estacion inicial: ").strip().upper()
            if inicio in sistema_tron:
                simulador.dijkstra_consola(inicio)
            else:
                print("Estacion no valida en el sistema Tron")
                
        # OPCIÓN 2: Modo gráfico con visualización
        elif opcion == '2':
            print("\nEstaciones disponibles:", list(sistema_tron.keys()))
            inicio = input("Ingrese estacion inicial: ").strip().upper()
            destino = input("Ingrese estacion destino (opcional): ").strip().upper()
            
            if inicio in sistema_tron:
                if destino and destino in sistema_tron:
                    simulador.dijkstra_grafico(inicio, destino)
                else:
                    simulador.dijkstra_grafico(inicio)
            else:
                print("Estacion no valida en el sistema Tron")
                
        # OPCIÓN 3: Salir del programa
        elif opcion == '3':
            print("Desconectando del sistema Tron...")
            break
        else:
            print("Opcion no reconocida por el sistema")

if __name__ == "__main__":
    # Punto de entrada del programa
    main()