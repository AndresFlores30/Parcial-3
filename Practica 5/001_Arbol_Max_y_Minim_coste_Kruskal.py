import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class KruskalSimulator:
    def __init__(self, grafo):
        self.grafo = grafo
        self.nodos = list(grafo.keys())
        self.aristas = self._obtener_aristas()
        
    def _obtener_aristas(self):
        """Extrae todas las aristas únicas del grafo"""
        aristas = set()
        for nodo in self.grafo:
            for vecino, peso in self.grafo[nodo]:
                # Ordenar para evitar duplicados A-B y B-A
                arista_ordenada = tuple(sorted([nodo, vecino])) + (peso,)
                aristas.add(arista_ordenada)
        return sorted(list(aristas), key=lambda x: x[2])  # Ordenar por peso
    
    def _encontrar(self, padre, nodo):
        """Encuentra la raíz de un nodo en el conjunto disjunto"""
        if padre[nodo] != nodo:
            padre[nodo] = self._encontrar(padre, padre[nodo])
        return padre[nodo]
    
    def _unir(self, padre, rango, conjunto1, conjunto2):
        """Une dos conjuntos disjuntos"""
        raiz1 = self._encontrar(padre, conjunto1)
        raiz2 = self._encontrar(padre, conjunto2)
        
        if raiz1 != raiz2:
            if rango[raiz1] > rango[raiz2]:
                padre[raiz2] = raiz1
            elif rango[raiz1] < rango[raiz2]:
                padre[raiz1] = raiz2
            else:
                padre[raiz2] = raiz1
                rango[raiz1] += 1
            return True
        return False
    
    def kruskal_minimo_consola(self):
        """Algoritmo de Kruskal para árbol de expansión mínima"""
        print("=" * 70)
        print("ALGORITMO DE KRUSKAL - ÁRBOL DE EXPANSIÓN MÍNIMA")
        print("=" * 70)
        
        # Inicializar estructuras
        aristas_ordenadas = self.aristas.copy()
        padre = {nodo: nodo for nodo in self.nodos}
        rango = {nodo: 0 for nodo in self.nodos}
        mst = []
        costo_total = 0
        
        print("Aristas ordenadas por peso (menor a mayor):")
        for i, (u, v, peso) in enumerate(aristas_ordenadas, 1):
            print(f"  {i}. {u}-{v} (peso: {peso})")
        print()
        
        paso = 1
        
        for arista in aristas_ordenadas:
            u, v, peso = arista
            
            print(f"--- PASO {paso} ---")
            print(f"Procesando arista: {u}-{v} (peso: {peso})")
            print(f"Conjuntos actuales: {padre}")
            print(f"Aristas en MST: {mst}")
            print(f"Costo acumulado: {costo_total}")
            print()
            
            raiz_u = self._encontrar(padre, u)
            raiz_v = self._encontrar(padre, v)
            
            print(f"  Raíz de {u}: {raiz_u}")
            print(f"  Raíz de {v}: {raiz_v}")
            
            if raiz_u != raiz_v:
                # No forman ciclo, agregar al MST
                if self._unir(padre, rango, u, v):
                    mst.append((u, v, peso))
                    costo_total += peso
                    print(f"  ✓ AÑADIDA: {u}-{v} al MST")
                    print(f"  Conjuntos actualizados: {padre}")
                else:
                    print(f"  ✗ NO SE PUDO UNIR (error)")
            else:
                print(f"  ✗ DESCARTADA: Formaría ciclo")
            
            paso += 1
            print("-" * 50)
            
            if len(mst) == len(self.nodos) - 1:
                print("¡Se alcanzó el número máximo de aristas para el MST!")
                break
        
        # Resultados finales
        print("\n" + "=" * 70)
        print("RESULTADOS FINALES - ÁRBOL DE EXPANSIÓN MÍNIMA")
        print("=" * 70)
        print("Aristas del MST:")
        for i, (u, v, peso) in enumerate(mst, 1):
            print(f"  {i}. {u}-{v} (peso: {peso})")
        print(f"\nCosto total: {costo_total}")
        print(f"Nodos conectados: {len(set([nodo for arista in mst for nodo in arista[:2]]))}")
        print(f"Todos los nodos conectados: {len(set([nodo for arista in mst for nodo in arista[:2]])) == len(self.nodos)}")
        
        return mst, costo_total
    
    def kruskal_maximo_consola(self):
        """Algoritmo de Kruskal para árbol de expansión máxima"""
        print("=" * 70)
        print("ALGORITMO DE KRUSKAL - ÁRBOL DE EXPANSIÓN MÁXIMA")
        print("=" * 70)
        
        # Ordenar aristas en orden descendente
        aristas_ordenadas = sorted(self.aristas, key=lambda x: x[2], reverse=True)
        
        # Inicializar estructuras
        padre = {nodo: nodo for nodo in self.nodos}
        rango = {nodo: 0 for nodo in self.nodos}
        mst = []
        costo_total = 0
        
        print("Aristas ordenadas por peso (mayor a menor):")
        for i, (u, v, peso) in enumerate(aristas_ordenadas, 1):
            print(f"  {i}. {u}-{v} (peso: {peso})")
        print()
        
        paso = 1
        
        for arista in aristas_ordenadas:
            u, v, peso = arista
            
            print(f"--- PASO {paso} ---")
            print(f"Procesando arista: {u}-{v} (peso: {peso})")
            print(f"Conjuntos actuales: {padre}")
            print(f"Aristas en MST: {mst}")
            print(f"Costo acumulado: {costo_total}")
            print()
            
            raiz_u = self._encontrar(padre, u)
            raiz_v = self._encontrar(padre, v)
            
            print(f"  Raíz de {u}: {raiz_u}")
            print(f"  Raíz de {v}: {raiz_v}")
            
            if raiz_u != raiz_v:
                # No forman ciclo, agregar al MST
                if self._unir(padre, rango, u, v):
                    mst.append((u, v, peso))
                    costo_total += peso
                    print(f"  ✓ AÑADIDA: {u}-{v} al MST")
                    print(f"  Conjuntos actualizados: {padre}")
                else:
                    print(f"  ✗ NO SE PUDO UNIR (error)")
            else:
                print(f"  ✗ DESCARTADA: Formaría ciclo")
            
            paso += 1
            print("-" * 50)
            
            if len(mst) == len(self.nodos) - 1:
                print("¡Se alcanzó el número máximo de aristas para el MST!")
                break
        
        # Resultados finales
        print("\n" + "=" * 70)
        print("RESULTADOS FINALES - ÁRBOL DE EXPANSIÓN MÁXIMA")
        print("=" * 70)
        print("Aristas del MST:")
        for i, (u, v, peso) in enumerate(mst, 1):
            print(f"  {i}. {u}-{v} (peso: {peso})")
        print(f"\nCosto total: {costo_total}")
        print(f"Nodos conectados: {len(set([nodo for arista in mst for nodo in arista[:2]]))}")
        
        return mst, costo_total
    
    def visualizar_kruskal(self, mst_min, mst_max, costo_min, costo_max):
        """Visualización gráfica comparativa de ambos algoritmos"""
        print("\n" + "=" * 70)
        print("VISUALIZACIÓN GRÁFICA - COMPARATIVA KRUSKAL")
        print("=" * 70)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Crear grafo completo
        G = nx.Graph()
        for nodo in self.grafo:
            G.add_node(nodo)
            for vecino, peso in self.grafo[nodo]:
                G.add_edge(nodo, vecino, weight=peso)
        
        pos = nx.spring_layout(G, seed=42)
        
        # SUBGRÁFICO 1: Árbol de Expansión Mínima
        ax1.set_title(f"ÁRBOL DE EXPANSIÓN MÍNIMA\nCosto Total: {costo_min}", 
                     fontsize=14, fontweight='bold', color='green')
        
        # Dibujar grafo completo (fondo)
        nx.draw_networkx_nodes(G, pos, ax=ax1, node_size=500, 
                              node_color='lightgray', alpha=0.3)
        nx.draw_networkx_edges(G, pos, ax=ax1, alpha=0.2, 
                              edge_color='gray', style='dashed')
        nx.draw_networkx_labels(G, pos, ax=ax1, font_size=10)
        
        # Dibujar MST mínimo
        MST_min = nx.Graph()
        for u, v, peso in mst_min:
            MST_min.add_edge(u, v, weight=peso)
        
        nx.draw_networkx_edges(MST_min, pos, ax=ax1, width=3, 
                              edge_color='blue', alpha=0.8)
        nx.draw_networkx_nodes(G, pos, ax=ax1, nodelist=list(MST_min.nodes()), 
                              node_size=600, node_color='blue', alpha=0.8)
        
        # Etiquetas de pesos para MST mínimo
        edge_labels_min = {(u, v): f"{d['weight']}" for u, v, d in MST_min.edges(data=True)}
        nx.draw_networkx_edge_labels(MST_min, pos, ax=ax1, edge_labels=edge_labels_min,
                                   font_color='darkblue', font_weight='bold')
        
        # SUBGRÁFICO 2: Árbol de Expansión Máxima
        ax2.set_title(f"ÁRBOL DE EXPANSIÓN MÁXIMA\nCosto Total: {costo_max}", 
                     fontsize=14, fontweight='bold', color='red')
        
        # Dibujar grafo completo (fondo)
        nx.draw_networkx_nodes(G, pos, ax=ax2, node_size=500, 
                              node_color='lightgray', alpha=0.3)
        nx.draw_networkx_edges(G, pos, ax=ax2, alpha=0.2, 
                              edge_color='gray', style='dashed')
        nx.draw_networkx_labels(G, pos, ax=ax2, font_size=10)
        
        # Dibujar MST máximo
        MST_max = nx.Graph()
        for u, v, peso in mst_max:
            MST_max.add_edge(u, v, weight=peso)
        
        nx.draw_networkx_edges(MST_max, pos, ax=ax2, width=3, 
                              edge_color='red', alpha=0.8)
        nx.draw_networkx_nodes(G, pos, ax=ax2, nodelist=list(MST_max.nodes()), 
                              node_size=600, node_color='red', alpha=0.8)
        
        # Etiquetas de pesos para MST máximo
        edge_labels_max = {(u, v): f"{d['weight']}" for u, v, d in MST_max.edges(data=True)}
        nx.draw_networkx_edge_labels(MST_max, pos, ax=ax2, edge_labels=edge_labels_max,
                                   font_color='darkred', font_weight='bold')
        
        # Configuración final
        for ax in [ax1, ax2]:
            ax.set_axis_off()
        
        plt.tight_layout()
        plt.show()
        
        # Mostrar comparativa
        print("\nCOMPARATIVA FINAL:")
        print(f"Árbol Mínimo - Costo: {costo_min}")
        print(f"Árbol Máximo - Costo: {costo_max}")
        print(f"Diferencia: {abs(costo_max - costo_min)}")

# Funciones para crear grafos de ejemplo
def crear_grafo_pequeno():
    """Grafo pequeño para demostración básica"""
    return {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8)],
        'D': [('B', 5), ('C', 8)]
    }

def crear_grafo_medio():
    """Grafo medio para demostración más compleja"""
    return {
        'A': [('B', 7), ('D', 5)],
        'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
        'C': [('B', 8), ('E', 5)],
        'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
        'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8)],
        'F': [('D', 6), ('E', 8)]
    }

def crear_grafo_complejo():
    """Grafo complejo con más nodos y conexiones"""
    return {
        'A': [('B', 4), ('C', 2), ('F', 3)],
        'B': [('A', 4), ('C', 1), ('D', 5), ('E', 6)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('F', 7)],
        'D': [('B', 5), ('C', 8), ('E', 2), ('G', 4)],
        'E': [('B', 6), ('D', 2), ('F', 3), ('G', 5)],
        'F': [('A', 3), ('C', 7), ('E', 3), ('G', 6)],
        'G': [('D', 4), ('E', 5), ('F', 6)]
    }

def main():
    """Función principal con menú interactivo"""
    print("SIMULADOR DEL ALGORITMO DE KRUSKAL")
    print("Árbol de Expansión Mínima y Máxima")
    print()
    
    # Selección de grafo
    print("Seleccione el grafo de ejemplo:")
    print("1. Grafo pequeño (4 nodos)")
    print("2. Grafo medio (6 nodos)") 
    print("3. Grafo complejo (7 nodos)")
    
    opcion_grafo = input("Opción (1-3): ").strip()
    
    if opcion_grafo == '1':
        grafo = crear_grafo_pequeno()
    elif opcion_grafo == '2':
        grafo = crear_grafo_medio()
    else:
        grafo = crear_grafo_complejo()
    
    simulador = KruskalSimulator(grafo)
    
    while True:
        print("\n" + "=" * 50)
        print("MENÚ PRINCIPAL - ALGORITMO DE KRUSKAL")
        print("=" * 50)
        print("1. Ejecutar Kruskal Mínimo (consola)")
        print("2. Ejecutar Kruskal Máximo (consola)")
        print("3. Ejecutar ambos y comparar (con gráficos)")
        print("4. Mostrar grafo completo")
        print("5. Salir")
        
        opcion = input("\nSeleccione opción (1-5): ").strip()
        
        if opcion == '1':
            print()
            mst_min, costo_min = simulador.kruskal_minimo_consola()
            
        elif opcion == '2':
            print()
            mst_max, costo_max = simulador.kruskal_maximo_consola()
            
        elif opcion == '3':
            print("\nEjecutando ambos algoritmos...")
            print()
            mst_min, costo_min = simulador.kruskal_minimo_consola()
            print("\n" + "="*70)
            mst_max, costo_max = simulador.kruskal_maximo_consola()
            simulador.visualizar_kruskal(mst_min, mst_max, costo_min, costo_max)
            
        elif opcion == '4':
            print("\nGRAFO COMPLETO:")
            print("Nodos y conexiones:")
            for nodo, conexiones in grafo.items():
                print(f"  {nodo}: {conexiones}")
            print(f"\nTotal de nodos: {len(grafo)}")
            print(f"Total de aristas únicas: {len(simulador.aristas)}")
            
        elif opcion == '5':
            print("Saliendo del simulador...")
            break
            
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()