class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def run(self, start):
        grafo = self.graph.nodes

        no_visitados = list(grafo.keys())
        distancias = {nodo: float('inf') for nodo in grafo}
        distancias[start] = 0
        sucesores = {nodo: set() for nodo in grafo}

        # PROCESO PRINCIPAL (igual que tu código)
        while no_visitados:
            nodo_actual = min(no_visitados, key=lambda n: distancias[n])

            if distancias[nodo_actual] == float('inf'):
                break

            no_visitados.remove(nodo_actual)

            for vecino, peso in grafo[nodo_actual]:
                nueva_dist = distancias[nodo_actual] + peso

                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    sucesores[vecino] = {nodo_actual}

                elif nueva_dist == distancias[vecino]:
                    sucesores[vecino].add(nodo_actual)

        # FUNCIÓN RECURSIVA (igual que tu código)
        def reunir_sucesores(nodo):
            if nodo == start:
                return set()
            total = set()
            for s in sucesores[nodo]:
                total.add(s)
                total.update(reunir_sucesores(s))
            return total

        # TABLA DE RESULTADOS (igual que tu versión)
        tabla = {}
        for nodo in grafo:
            if nodo == start:
                tabla[nodo] = [0, ["ninguno"]]
            else:
                todos_sucesores = reunir_sucesores(nodo)
                if not todos_sucesores:
                    todos_sucesores = {"ninguno"}
                tabla[nodo] = [distancias[nodo], list(todos_sucesores)]

        return tabla

    # Método adicional útil para tu app: obtener la distancia a un nodo
    def distancia_hasta(self, start, end):
        tabla = self.run(start)
        return tabla[end][0]

    # Obtiene la ruta mínima reconstruyendo sucesores
    def ruta_minima(self, start, end):
        tabla = self.run(start)

        # reconstrucción básica
        ruta = [end]
        actuales = tabla[end][1]

        while "ninguno" not in actuales:
            primero = list(actuales)[0]  # tomar uno
            ruta.append(primero)
            actuales = tabla[primero][1]

        return list(reversed(ruta))
