import heapq
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class PrimMSTSimulator:
    def __init__(self, grafo):
        self.grafo = grafo
        self.nodos = list(grafo.keys())
        
    def prim_consola(self, inicio):
        print("=" * 60)
        print("ALGORITMO DE PRIM - ÁRBOL DE EXPANSIÓN MÍNIMA")
        print("=" * 60)
        print(f"Nodo inicial: {inicio}")
        print()
        
        # Estructuras para el algoritmo
        visitados = set([inicio])
        aristas_mst = []
        cola_aristas = []
        costo_total = 0
        
        # Inicializar con las aristas del nodo inicial
        for vecino, peso in self.grafo[inicio]:
            heapq.heappush(cola_aristas, (peso, inicio, vecino))
        
        paso = 1
        
        while cola_aristas and len(visitados) < len(self.nodos):
            print(f"--- PASO {paso} ---")
            print(f"Nodos visitados: {sorted(visitados)}")
            print(f"Aristas en cola de prioridad: {cola_aristas}")
            print(f"Aristas en MST: {aristas_mst}")
            print(f"Costo acumulado: {costo_total}")
            print()
            
            # Extraer la arista con menor peso
            peso, nodo_a, nodo_b = heapq.heappop(cola_aristas)
            
            print(f"Procesando arista: {nodo_a}-{nodo_b} (peso: {peso})")
            
            if nodo_b not in visitados:
                # Agregar la arista al MST
                aristas_mst.append((nodo_a, nodo_b, peso))
                costo_total += peso
                visitados.add(nodo_b)
                
                print(f"✓ AÑADIDA al MST: {nodo_a}-{nodo_b}")
                print(f"  Nodo {nodo_b} agregado a visitados")
                
                # Agregar nuevas aristas del nodo recién visitado
                for vecino, peso_vecino in self.grafo[nodo_b]:
                    if vecino not in visitados:
                        heapq.heappush(cola_aristas, (peso_vecino, nodo_b, vecino))
                        print(f"  + Arista agregada a cola: {nodo_b}-{vecino} (peso: {peso_vecino})")
            else:
                print(f"✗ DESCARTADA: {nodo_b} ya está visitado")
            
            paso += 1
            print("-" * 40)
        
        # Resultados finales
        print("\n" + "=" * 60)
        print("RESULTADOS FINALES - ÁRBOL DE EXPANSIÓN MÍNIMA")
        print("=" * 60)
        print(f"Aristas del MST: {aristas_mst}")
        print(f"Costo total: {costo_total}")
        print(f"Nodos conectados: {sorted(visitados)}")
        print(f"Todos los nodos conectados: {len(visitados) == len(self.nodos)}")
        
        return aristas_mst, costo_total
    
    def prim_grafico(self, inicio):
        print("\n" + "=" * 60)
        print("VISUALIZACIÓN GRÁFICA - ALGORITMO DE PRIM")
        print("=" * 60)
        
        # Ejecutar Prim para obtener el MST
        aristas_mst, costo_total = self.prim_consola(inicio)
        
        # Crear visualización
        plt.figure(figsize=(15, 10))
        G = nx.Graph()
        
        # Agregar todos los nodos y aristas al grafo completo
        for nodo in self.grafo:
            G.add_node(nodo)
            for vecino, peso in self.grafo[nodo]:
                G.add_edge(nodo, vecino, weight=peso)
        
        # Posiciones para el gráfico
        pos = nx.spring_layout(G, seed=42)
        
        # Dibujar el grafo completo (todas las aristas posibles)
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', alpha=0.7)
        nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color='gray', style='dashed')
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
        
        # Etiquetas de pesos para todas las aristas
        edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        
        # Resaltar el MST
        if aristas_mst:
            # Crear subgrafo del MST
            MST = nx.Graph()
            for u, v, peso in aristas_mst:
                MST.add_edge(u, v, weight=peso)
            
            # Dibujar el MST encima
            nx.draw_networkx_edges(MST, pos, width=3, alpha=0.8, edge_color='red')
            nx.draw_networkx_nodes(G, pos, nodelist=list(MST.nodes()), 
                                 node_size=800, node_color='red', alpha=0.8)
        
        plt.title(f"Algoritmo de Prim - Árbol de Expansión Mínima\n"
                 f"Nodo inicial: {inicio} - Costo total: {costo_total}", 
                 fontsize=14, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
        return aristas_mst, costo_total

# Función para crear grafo de ejemplo
def crear_grafo_ejemplo():
    """Crea un grafo de ejemplo para demostrar el algoritmo de Prim"""
    grafo = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
        'E': [('C', 10), ('D', 2), ('F', 3)],
        'F': [('D', 6), ('E', 3)]
    }
    return grafo

def crear_grafo_grande():
    """Crea un grafo más grande para demostración"""
    grafo = {
        'A': [('B', 7), ('D', 5)],
        'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
        'C': [('B', 8), ('E', 5)],
        'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
        'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
        'F': [('D', 6), ('E', 8), ('G', 11)],
        'G': [('E', 9), ('F', 11)]
    }
    return grafo

# Función principal
def main():
    print("SIMULADOR DEL ALGORITMO DE PRIM")
    print("Árbol de Expansión Mínima (Minimum Spanning Tree)")
    print()
    
    # Seleccionar grafo
    print("Seleccione el grafo de ejemplo:")
    print("1. Grafo pequeño (6 nodos)")
    print("2. Grafo grande (7 nodos)")
    
    opcion_grafo = input("Opción (1-2): ").strip()
    
    if opcion_grafo == '1':
        grafo = crear_grafo_ejemplo()
    else:
        grafo = crear_grafo_grande()
    
    # Crear simulador
    simulador = PrimMSTSimulator(grafo)
    
    while True:
        print("\n" + "=" * 50)
        print("MENÚ PRINCIPAL - ALGORITMO DE PRIM")
        print("=" * 50)
        print("1. Ejecutar Prim en consola (paso a paso)")
        print("2. Ejecutar Prim con visualización gráfica")
        print("3. Mostrar grafo completo")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            print(f"\nNodos disponibles: {list(grafo.keys())}")
            inicio = input("Ingrese nodo inicial: ").strip().upper()
            if inicio in grafo:
                simulador.prim_consola(inicio)
            else:
                print("Error: Nodo no válido")
                
        elif opcion == '2':
            print(f"\nNodos disponibles: {list(grafo.keys())}")
            inicio = input("Ingrese nodo inicial: ").strip().upper()
            if inicio in grafo:
                simulador.prim_grafico(inicio)
            else:
                print("Error: Nodo no válido")
                
        elif opcion == '3':
            print("\nGRAFO COMPLETO:")
            print("Nodos y sus conexiones (nodo: [(vecino, peso), ...]):")
            for nodo, conexiones in grafo.items():
                print(f"  {nodo}: {conexiones}")
                
        elif opcion == '4':
            print("Saliendo del simulador...")
            break
            
        else:
            print("Opción no válida")

# Ejecutar demostración automática
def demostracion_automatica():
    """Ejecuta una demostración automática del algoritmo"""
    print("DEMOSTRACIÓN AUTOMÁTICA - ALGORITMO DE PRIM")
    print("=" * 50)
    
    grafo = crear_grafo_ejemplo()
    simulador = PrimMSTSimulator(grafo)
    
    print("Grafo de ejemplo:")
    for nodo, conexiones in grafo.items():
        print(f"  {nodo}: {conexiones}")
    
    print("\nEjecutando Prim desde el nodo 'A'...")
    print()
    
    aristas_mst, costo_total = simulador.prim_consola('A')
    
    print("\n" + "=" * 50)
    print("RESUMEN DE LA DEMOSTRACIÓN")
    print("=" * 50)
    print(f"Árbol de Expansión Mínima encontrado:")
    for arista in aristas_mst:
        print(f"  {arista[0]} - {arista[1]} (peso: {arista[2]})")
    print(f"Costo total: {costo_total}")

if __name__ == "__main__":
    # Preguntar si quiere demostración automática o menú interactivo
    print("BIENVENIDO AL SIMULADOR DE PRIM")
    print("1. Demostración automática")
    print("2. Modo interactivo")
    
    eleccion = input("Seleccione opción (1-2): ").strip()
    
    if eleccion == '1':
        demostracion_automatica()
    else:
        main()