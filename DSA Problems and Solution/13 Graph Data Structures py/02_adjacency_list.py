"""
Assignment-23: Adjacency List Implementation of Graph
1. Write a class Graph to implement list representation of a graph data structure.
2. In class Graph, define init_() method to initialise instance object variables vertex_count and a dict adj_list where key is vertex number and value is a list of adjacent vertices.
3. In class Graph, define add_edge() method to add an edge in the graph with given vertices and weight.
4. In class Graph, define remove_edge() method to remove an edge from the graph.
5. In class Graph, define has_edge() method to check whether an edge exists or not for a given pair of vertices.
6.In class Graph, define print_adj_list() method to print adjacency lists of graph.
"""

class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = {i: [] for i in range(vertex_count)}

    def add_edge(self, u, v, weight = 1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Invalid Vertex")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u] = [(vertex, weight) for vertex, weight in self.adj_list[u] if vertex != v]
            self.adj_list[v] = [(vertex, weight) for vertex, weight in self.adj_list[v] if vertex != u]
        else:
            print("Invalid Vertex")

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return any(vertex == v for vertex, x in self.adj_list[u])
        else:
            print("Invalid Vertex")

    def print_adj_list(self):
        for vertex, n in self.adj_list.items():
            print(f"V {vertex}: {n}")


g = Graph(5)

g.add_edge(0, 1, 2)
g.add_edge(1, 2, 3)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 5)

print("Adjacency List:")
g.print_adj_list()

print("\nDoes an edge exist between 1 and 2?", g.has_edge(1, 2))

g.remove_edge(1, 2)

print("\nDoes an edge exist between 1 and 2 after removal?", g.has_edge(1, 2))

print("\nUpdated Adjacency List:")
g.print_adj_list()
