class Graph:
    def __init__(self):
        self.nodes = {}   #deben estar en este formato { "A": [("B", peso), ("C", peso)] }

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = []

    def add_edge(self, a, b, weight, bidirectional=True):
        self.add_node(a)
        self.add_node(b)
        self.nodes[a].append((b, weight))
        if bidirectional:
            self.nodes[b].append((a, weight))

    def get_neighbors(self, node_id):
        return self.nodes.get(node_id, [])

    def __repr__(self):
        return f"Graph({self.nodes})"

