import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class DeliveryOptimizer:
    def __init__(self, zonas):
        self.zonas = zonas
        self.nodos = list(zonas.keys())
        self.conexiones = self._obtener_conexiones()
        
    def _obtener_conexiones(self):
        """Extrae todas las conexiones únicas entre zonas"""
        conexiones = set()
        for zona in self.zonas:
            for vecino, distancia in self.zonas[zona]:
                # Ordenar para evitar duplicados
                conexion_ordenada = tuple(sorted([zona, vecino])) + (distancia,)
                conexiones.add(conexion_ordenada)
        return sorted(list(conexiones), key=lambda x: x[2])
    
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
    
    def ruta_delivery_optima(self):
        """Encuentra la ruta de delivery más eficiente (menor distancia total)"""
        print("=" * 70)
        print("OPTIMIZADOR DE RUTAS DE DELIVERY")
        print("=" * 70)
        print("Buscando la conexión más eficiente entre zonas de reparto")
        print()
        
        # Inicializar estructuras
        conexiones_ordenadas = self.conexiones.copy()
        padre = {zona: zona for zona in self.nodos}
        rango = {zona: 0 for zona in self.nodos}
        ruta_optima = []
        distancia_total = 0
        
        print("Distancias entre zonas ordenadas (de menor a mayor):")
        for i, (zona1, zona2, distancia) in enumerate(conexiones_ordenadas, 1):
            print(f"  {i}. {zona1} - {zona2}: {distancia} km")
        print()
        
        paso = 1
        
        for conexion in conexiones_ordenadas:
            zona1, zona2, distancia = conexion
            
            print(f"--- ANÁLISIS {paso} ---")
            print(f"Evaluando conexión: {zona1} - {zona2} (distancia: {distancia} km)")
            print(f"Conexiones actualmente seleccionadas: {ruta_optima}")
            print(f"Distancia acumulada: {distancia_total} km")
            print()
            
            raiz1 = self._encontrar(padre, zona1)
            raiz2 = self._encontrar(padre, zona2)
            
            print(f"  Grupo de {zona1}: {raiz1}")
            print(f"  Grupo de {zona2}: {raiz2}")
            
            if raiz1 != raiz2:
                # No forman ciclo, se puede agregar a la ruta
                if self._unir(padre, rango, zona1, zona2):
                    ruta_optima.append((zona1, zona2, distancia))
                    distancia_total += distancia
                    print(f"  ✓ CONEXION AGREGADA: Conecta {zona1} con {zona2}")
                    print(f"  Grupos actualizados: {padre}")
                else:
                    print(f"  ✗ ERROR: No se pudo establecer la conexión")
            else:
                print(f"  ✗ CONEXION DESCARTADA: Las zonas ya están conectadas (evitaría duplicar rutas)")
            
            paso += 1
            print("-" * 50)
            
            if len(ruta_optima) == len(self.nodos) - 1:
                print("¡Se ha encontrado la red de conexiones óptima!")
                break
        
        # Resultados finales
        print("\n" + "=" * 70)
        print("RUTA DE DELIVERY OPTIMIZADA")
        print("=" * 70)
        print("Conexiones seleccionadas (rutas a utilizar):")
        for i, (zona1, zona2, distancia) in enumerate(ruta_optima, 1):
            print(f"  {i}. {zona1} ↔ {zona2}: {distancia} km")
        
        zonas_conectadas = set()
        for zona1, zona2, _ in ruta_optima:
            zonas_conectadas.add(zona1)
            zonas_conectadas.add(zona2)
        
        print(f"\nRESUMEN:")
        print(f"  Distancia total de la red: {distancia_total} km")
        print(f"  Zonas conectadas: {len(zonas_conectadas)} de {len(self.nodos)}")
        print(f"  Ahorro estimado: {self._calcular_ahorro(distancia_total)} km vs conectar todas las rutas")
        
        return ruta_optima, distancia_total
    
    def _calcular_ahorro(self, distancia_optima):
        """Calcula el ahorro vs conectar todas las zonas directamente"""
        distancia_total_posible = 0
        for zona1 in self.nodos:
            for zona2, distancia in self.zonas[zona1]:
                if zona1 < zona2:  # Evitar duplicados
                    distancia_total_posible += distancia
        
        ahorro = distancia_total_posible - distancia_optima
        return round(ahorro, 1)
    
    def visualizar_mapa_delivery(self, ruta_optima, distancia_total):
        """Visualización del mapa de delivery optimizado"""
        print("\n" + "=" * 70)
        print("MAPA DE ZONAS DE REPARTO - RUTA OPTIMIZADA")
        print("=" * 70)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
        
        # Crear grafo completo
        G = nx.Graph()
        for zona in self.zonas:
            G.add_node(zona)
            for vecino, distancia in self.zonas[zona]:
                G.add_edge(zona, vecino, weight=distancia)
        
        # Posiciones para los nodos (simulando ubicaciones geográficas)
        pos = nx.spring_layout(G, seed=42, k=3, iterations=50)
        
        # SUBGRÁFICO 1: Mapa completo (todas las rutas posibles)
        ax1.set_title("TODAS LAS RUTAS POSIBLES\n(Sin optimizar)", 
                     fontsize=14, fontweight='bold', color='gray')
        
        # Dibujar todas las rutas posibles
        nx.draw_networkx_nodes(G, pos, ax=ax1, node_size=600, 
                              node_color='lightblue', alpha=0.8,
                              edgecolors='blue', linewidths=2)
        nx.draw_networkx_edges(G, pos, ax=ax1, alpha=0.3, 
                              edge_color='gray', width=1)
        nx.draw_networkx_labels(G, pos, ax=ax1, font_size=10, font_weight='bold')
        
        # Calcular distancia total sin optimizar
        dist_total_no_opt = sum(d for _, _, d in self.conexiones)
        ax1.set_xlabel(f"Distancia total disponible: {dist_total_no_opt} km", fontsize=10)
        
        # SUBGRÁFICO 2: Ruta optimizada
        ax2.set_title(f"RUTA DE DELIVERY OPTIMIZADA\nDistancia total: {distancia_total} km", 
                     fontsize=14, fontweight='bold', color='green')
        
        # Dibujar todas las zonas
        nx.draw_networkx_nodes(G, pos, ax=ax2, node_size=600, 
                              node_color='lightgreen', alpha=0.8,
                              edgecolors='darkgreen', linewidths=2)
        nx.draw_networkx_labels(G, pos, ax=ax2, font_size=10, font_weight='bold')
        
        # Dibujar solo la ruta optimizada
        G_opt = nx.Graph()
        for zona1, zona2, distancia in ruta_optima:
            G_opt.add_edge(zona1, zona2, weight=distancia)
        
        nx.draw_networkx_edges(G_opt, pos, ax=ax2, width=3, 
                              edge_color='green', alpha=0.9)
        
        # Etiquetas de distancias para la ruta optimizada
        edge_labels = {(z1, z2): f"{d} km" for z1, z2, d in ruta_optima}
        nx.draw_networkx_edge_labels(G_opt, pos, ax=ax2, 
                                     edge_labels=edge_labels,
                                     font_color='darkgreen', 
                                     font_size=9,
                                     font_weight='bold')
        
        # Configuración final
        for ax in [ax1, ax2]:
            ax.set_axis_off()
        
        # Información adicional
        ahorro = self._calcular_ahorro(distancia_total)
        info_text = f"Ahorro estimado: {ahorro} km\n"
        info_text += f"Eficiencia: {round((1 - distancia_total/dist_total_no_opt)*100, 1)}%"
        
        plt.figtext(0.5, 0.02, info_text, 
                   fontsize=12, ha='center',
                   bbox=dict(boxstyle="round", facecolor='lightyellow', 
                           edgecolor='gray', alpha=0.9))
        
        plt.tight_layout()
        plt.show()

def crear_zonas_residenciales():
    """Crea un mapa de zonas residenciales con distancias realistas"""
    return {
        'NORTE': [('CENTRO', 5.2), ('ESTE', 4.8), ('OESTE', 6.1)],
        'SUR': [('CENTRO', 4.5), ('ESTE', 7.3), ('OESTE', 3.9)],
        'ESTE': [('CENTRO', 3.8), ('NORTE', 4.8), ('SUR', 7.3)],
        'OESTE': [('CENTRO', 4.2), ('NORTE', 6.1), ('SUR', 3.9)],
        'CENTRO': [('NORTE', 5.2), ('SUR', 4.5), ('ESTE', 3.8), ('OESTE', 4.2)]
    }

def crear_barrios_ciudad():
    """Crea un mapa más detallado de barrios de una ciudad"""
    return {
        'CENTRO': [('NORTE', 4.5), ('SUR', 5.2), ('ESTE', 3.8), ('OESTE', 4.0)],
        'NORTE': [('CENTRO', 4.5), ('INDUSTRIAL', 6.2), ('RESIDENCIAL_A', 2.8)],
        'SUR': [('CENTRO', 5.2), ('PLAYA', 3.5), ('RESIDENCIAL_B', 4.1)],
        'ESTE': [('CENTRO', 3.8), ('UNIVERSIDAD', 2.5), ('PARQUE', 3.3)],
        'OESTE': [('CENTRO', 4.0), ('SHOPPING', 2.2), ('RESIDENCIAL_C', 3.7)],
        'INDUSTRIAL': [('NORTE', 6.2), ('PUERTO', 5.8)],
        'PLAYA': [('SUR', 3.5), ('RESIDENCIAL_B', 2.9)],
        'UNIVERSIDAD': [('ESTE', 2.5), ('PARQUE', 1.8)],
        'PARQUE': [('ESTE', 3.3), ('UNIVERSIDAD', 1.8)],
        'SHOPPING': [('OESTE', 2.2), ('RESIDENCIAL_C', 2.5)],
        'RESIDENCIAL_A': [('NORTE', 2.8)],
        'RESIDENCIAL_B': [('SUR', 4.1), ('PLAYA', 2.9)],
        'RESIDENCIAL_C': [('OESTE', 3.7), ('SHOPPING', 2.5)],
        'PUERTO': [('INDUSTRIAL', 5.8)]
    }

def crear_zonas_comerciales():
    """Crea un mapa de zonas comerciales para delivery de comercios"""
    return {
        'MERCADO': [('RESTAURANTES', 2.3), ('OFICINAS', 3.5), ('TIENDAS', 2.8)],
        'RESTAURANTES': [('MERCADO', 2.3), ('OFICINAS', 1.5), ('BARES', 1.2)],
        'OFICINAS': [('MERCADO', 3.5), ('RESTAURANTES', 1.5), ('TIENDAS', 2.1), ('BANCOS', 1.8)],
        'TIENDAS': [('MERCADO', 2.8), ('OFICINAS', 2.1), ('CENTRO_COMERCIAL', 3.0)],
        'BARES': [('RESTAURANTES', 1.2), ('CENTRO_COMERCIAL', 2.5)],
        'BANCOS': [('OFICINAS', 1.8), ('CENTRO_COMERCIAL', 2.2)],
        'CENTRO_COMERCIAL': [('TIENDAS', 3.0), ('BARES', 2.5), ('BANCOS', 2.2)]
    }

def main():
    """Función principal con menú interactivo"""
    print("OPTIMIZADOR DE RUTAS DE DELIVERY")
    print("Sistema para encontrar la red de rutas más eficiente")
    print()
    
    # Selección del mapa
    print("Seleccione el tipo de zona:")
    print("1. Zonas residenciales básicas (5 zonas)")
    print("2. Barrios de ciudad (14 zonas)")
    print("3. Zonas comerciales (7 zonas)")
    
    opcion_mapa = input("Opción (1-3): ").strip()
    
    if opcion_mapa == '1':
        zonas = crear_zonas_residenciales()
        tipo = "residenciales básicas"
    elif opcion_mapa == '2':
        zonas = crear_barrios_ciudad()
        tipo = "barrios de ciudad"
    else:
        zonas = crear_zonas_comerciales()
        tipo = "comerciales"
    
    optimizador = DeliveryOptimizer(zonas)
    
    while True:
        print(f"\n" + "=" * 50)
        print(f"MENÚ - OPTIMIZADOR DE DELIVERY ({tipo})")
        print("=" * 50)
        print("1. Calcular ruta de delivery óptima")
        print("2. Ver mapa de rutas optimizado")
        print("3. Ver todas las zonas disponibles")
        print("4. Cambiar tipo de zona")
        print("5. Salir")
        
        opcion = input("\nSeleccione opción (1-5): ").strip()
        
        if opcion == '1':
            print()
            ruta_optima, distancia_total = optimizador.ruta_delivery_optima()
            
        elif opcion == '2':
            print()
            ruta_optima, distancia_total = optimizador.ruta_delivery_optima()
            optimizador.visualizar_mapa_delivery(ruta_optima, distancia_total)
            
        elif opcion == '3':
            print("\nZONAS DE REPARTO DISPONIBLES:")
            print("Zona | Conexiones (zona - distancia en km)")
            print("-" * 50)
            
            for zona, conexiones in sorted(zonas.items()):
                print(f"{zona}:")
                for vecino, distancia in sorted(conexiones):
                    print(f"  → {vecino}: {distancia} km")
                print()
            
            print(f"Total de zonas: {len(zonas)}")
            print(f"Total de rutas posibles: {len(optimizador.conexiones)}")
            
        elif opcion == '4':
            print("\nVolviendo al menú de selección de zonas...")
            return main()
            
        elif opcion == '5':
            print("Gracias por usar el optimizador de delivery. ¡Hasta pronto!")
            break
            
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()