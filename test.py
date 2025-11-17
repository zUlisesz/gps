from models.graph import Graph
from models.dijkstra import Dijkstra


g = Graph()
g.add_edge("nodoA", "nodoB", 4)
g.add_edge("nodoA", "nodoC", 2)
g.add_edge("nodoB", "nodoC", 1)
g.add_edge("nodoB", "nodoD", 5)
g.add_edge("nodoC", "nodoD", 8)
g.add_edge("nodoC", "nodoE", 10)
g.add_edge("nodoD", "nodoE", 2)
g.add_edge("nodoD", "nodoF", 6)
g.add_edge("nodoE", "nodoF", 3)

d = Dijkstra(g)
tabla = d.run("nodoA")
print(tabla)

print("sistancia de A aF:", d.distancia_hasta("nodoA", "nodoF"))
print("camino de A a F:", d.ruta_minima("nodoA", "nodoF"))
