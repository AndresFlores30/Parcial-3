import heapq
import matplotlib.pyplot as plt
import networkx as nx

class CineDijkstraSimulator:
    def __init__(self, grafo):
        self.grafo = grafo
        self.nodos = list(grafo.keys())

    # -------------------------------
    # Normalización flexible
    # -------------------------------
    def normalizar(self, texto: str) -> str:
        return (
            texto.strip()
            .lower()
            .replace("_", "")
            .replace(" ", "")
            .replace("-", "")
        )

    def encontrar_nodo(self, entrada_usuario: str):
        entrada = self.normalizar(entrada_usuario)

        # 1) match exacto normalizado
        for nodo in self.nodos:
            if entrada == self.normalizar(nodo):
                return nodo

        # 2) match parcial (entrada dentro del nombre del nodo)
        for nodo in self.nodos:
            if entrada and entrada in self.normalizar(nodo):
                return nodo

        return None

    # -------------------------------
    # Construcción de grafo NetworkX
    # -------------------------------
    def construir_nx(self):
        G = nx.Graph()
        for nodo in self.grafo:
            G.add_node(nodo)
            for conexion, tiempo in self.grafo[nodo]:
                G.add_edge(nodo, conexion, weight=tiempo)
        return G

    # -------------------------------
    # Dibujar mapa (con ruta verde)
    # -------------------------------
    def dibujar_mapa(self, inicio=None, destino=None, ruta=None, tiempo_total=None, titulo_extra=""):
        plt.figure(figsize=(14, 10))
        plt.style.use("dark_background")

        fig = plt.gcf()
        fig.patch.set_facecolor("#1a1a1a")

        G = self.construir_nx()
        pos = nx.spring_layout(G, seed=42, k=2, iterations=70)

        # ---- Aristas base (azul claro)
        nx.draw_networkx_edges(G, pos, alpha=0.55, width=2)

        # ---- Nodos base (amarillo)
        nx.draw_networkx_nodes(G, pos, node_size=850, alpha=0.85)
        nx.draw_networkx_labels(
            G, pos,
            font_size=10,
            font_weight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#333333", edgecolor="#FFD700", alpha=0.75)
        )

        # ---- Pesos
        edge_labels = {(u, v): f"{d['weight']} min" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=edge_labels,
            font_size=8,
            bbox=dict(boxstyle="round", facecolor="#444444", edgecolor="#87CEEB", alpha=0.85)
        )

        # ---- Marcar inicio (azul)
        if inicio is not None:
            nx.draw_networkx_nodes(
                G, pos, nodelist=[inicio],
                node_size=1300, alpha=0.95
            )

        # ---- Marcar destino (rojo)
        if destino is not None:
            nx.draw_networkx_nodes(
                G, pos, nodelist=[destino],
                node_size=1400, alpha=0.95
            )

        # ---- Ruta en VERDE (lo que pediste)
        if ruta and len(ruta) >= 2:
            edges_ruta = [(ruta[i], ruta[i+1]) for i in range(len(ruta) - 1)]
            nx.draw_networkx_edges(
                G, pos,
                edgelist=edges_ruta,
                width=6,
                alpha=0.95,
                edge_color="#32CD32"  # verde brillante
            )
            nx.draw_networkx_nodes(
                G, pos,
                nodelist=ruta,
                node_size=1050,
                alpha=0.55,
                node_color="#32CD32"
            )

        # ---- Título
        if inicio and destino and tiempo_total is not None:
            titulo = f"RUTA AL CINE\n{inicio} → {destino} | Tiempo: {tiempo_total} min"
        elif inicio and destino:
            titulo = f"MAPA\n{inicio} → {destino}"
        else:
            titulo = "MAPA DE LA CIUDAD"

        if titulo_extra:
            titulo += f"\n{titulo_extra}"

        plt.title(titulo, fontsize=16, fontweight="bold", pad=18)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    # -------------------------------
    # Dijkstra
    # -------------------------------
    def dijkstra(self, inicio, destino):
        distancias = {n: float("inf") for n in self.nodos}
        distancias[inicio] = 0
        predecesores = {n: None for n in self.nodos}
        visitados = set()
        cola = [(0, inicio)]

        while cola:
            dist, actual = heapq.heappop(cola)

            if actual in visitados:
                continue
            visitados.add(actual)

            if actual == destino:
                break

            for vecino, w in self.grafo[actual]:
                if vecino in visitados:
                    continue
                nd = dist + w
                if nd < distancias[vecino]:
                    distancias[vecino] = nd
                    predecesores[vecino] = actual
                    heapq.heappush(cola, (nd, vecino))

        return distancias, predecesores

    def reconstruir_ruta(self, predecesores, inicio, destino):
        ruta = []
        actual = destino
        while actual is not None:
            ruta.append(actual)
            actual = predecesores[actual]
        ruta.reverse()
        return ruta if ruta and ruta[0] == inicio else None

    # -------------------------------
    # Opción 1: Consola + resultado y ruta VERDE
    # -------------------------------
    def opcion1_consola(self, inicio, destino):
        distancias, predecesores = self.dijkstra(inicio, destino)
        ruta = self.reconstruir_ruta(predecesores, inicio, destino)

        print("\n" + "=" * 60)
        print("RESULTADO FINAL - RUTA AL CINE")
        print("=" * 60)

        if ruta:
            print(f"Ruta más corta a '{destino}':")
            print(f"  Recorrido: {' → '.join(ruta)}")
            print(f"  Tiempo total: {distancias[destino]} minutos")
            print(f"  Número de paradas: {len(ruta) - 1}")

            # 👇 Aquí se marca la ruta en VERDE (resultado)
            self.dibujar_mapa(
                inicio=inicio,
                destino=destino,
                ruta=ruta,
                tiempo_total=distancias[destino],
                titulo_extra="(Ruta marcada en VERDE)"
            )
        else:
            print("No se encontró una ruta disponible.")

        return distancias, predecesores

    # -------------------------------
    # Opción 2: Visualizar mapa (gráfico)
    # -------------------------------
    def opcion2_visualizar(self, inicio=None, destino=None):
        # Si no te dan inicio/destino, solo muestra el mapa completo
        if inicio is None or destino is None:
            self.dibujar_mapa(titulo_extra="(Vista general del mapa)")
            return

        # Si te dan inicio/destino, muestra mapa y también la ruta
        distancias, predecesores = self.dijkstra(inicio, destino)
        ruta = self.reconstruir_ruta(predecesores, inicio, destino)

        if ruta:
            self.dibujar_mapa(
                inicio=inicio,
                destino=destino,
                ruta=ruta,
                tiempo_total=distancias[destino],
                titulo_extra="(Visualización con ruta)"
            )
        else:
            self.dibujar_mapa(
                inicio=inicio,
                destino=destino,
                ruta=None,
                tiempo_total=None,
                titulo_extra="(No se encontró ruta)"
            )


# -------------------------------
# Grafo con CINEPOLIS y CINEMEX
# -------------------------------
def crear_mapa_ciudad():
    return {
        "PLAZA_CENTRAL": [("MERCADO", 5), ("ESTACION_TREN", 8), ("PARQUE", 3)],
        "MERCADO": [("PLAZA_CENTRAL", 5), ("BIBLIOTECA", 4), ("CINEPOLIS", 7)],
        "ESTACION_TREN": [("PLAZA_CENTRAL", 8), ("UNIVERSIDAD", 6), ("CINEMEX", 10)],
        "PARQUE": [("PLAZA_CENTRAL", 3), ("BIBLIOTECA", 2), ("ESTADIO", 5)],
        "BIBLIOTECA": [("MERCADO", 4), ("PARQUE", 2), ("UNIVERSIDAD", 3)],
        "UNIVERSIDAD": [("ESTACION_TREN", 6), ("BIBLIOTECA", 3), ("CINEMEX", 4)],
        "ESTADIO": [("PARQUE", 5), ("CINEPOLIS", 6), ("CINEMEX", 7)],
        "CINEPOLIS": [("MERCADO", 7), ("ESTADIO", 6)],
        "CINEMEX": [("ESTACION_TREN", 10), ("UNIVERSIDAD", 4), ("ESTADIO", 7)],
    }


def main():
    mapa = crear_mapa_ciudad()
    sim = CineDijkstraSimulator(mapa)
    cines = ["CINEPOLIS", "CINEMEX"]

    while True:
        print("\n" + "=" * 60)
        print("SISTEMA DE RUTAS AL CINE")
        print("=" * 60)
        print("1. Buscar ruta")
        print("2. Visualizar mapa (gráfico)")
        print("3. Salir")

        opcion = input("\nSeleccione opción (1-3): ").strip()

        if opcion == "1":
            print("\nUbicaciones disponibles:", list(mapa.keys()))
            inicio_in = input("Ingrese punto de partida: ")
            inicio = sim.encontrar_nodo(inicio_in)

            if inicio is None:
                print("Ubicación no válida.")
                continue

            cine_in = input("Ingrese cine destino (Cinepolis / Cinemex): ")
            destino = sim.encontrar_nodo(cine_in)

            if destino not in cines:
                print("Cine no válido.")
                continue

            sim.opcion1_consola(inicio, destino)

        elif opcion == "2":
            print("\n1) Ver mapa general")
            print("2) Ver mapa + ruta (elige inicio y cine)")
            sub = input("Elige (1-2): ").strip()

            if sub == "1":
                sim.opcion2_visualizar()
            elif sub == "2":
                print("\nUbicaciones disponibles:", list(mapa.keys()))
                inicio_in = input("Ingrese punto de partida: ")
                inicio = sim.encontrar_nodo(inicio_in)

                if inicio is None:
                    print("Ubicación no válida.")
                    continue

                cine_in = input("Ingrese cine destino (Cinepolis / Cinemex): ")
                destino = sim.encontrar_nodo(cine_in)

                if destino not in cines:
                    print("Cine no válido.")
                    continue

                sim.opcion2_visualizar(inicio, destino)
            else:
                print("Opción no válida.")

        elif opcion == "3":
            print("Disfruta tu película 🍿")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()