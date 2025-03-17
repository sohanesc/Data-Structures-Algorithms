"""
Assignment-22: Adjacency Matrix implementation of Graph
1.	Write a class Graph to implement adjacency matrix representation of a simple and undirected graph.
2.	In class Graph, define init method to initialise vertex_count and adj_matrix (list of lists)
3.	In class Graph, define add_edge() method add an edge in the graph with given weight.
4.	In class Graph, define remove_edge() method to remove an edge from the graph.
5.	In class Graph, define has_edge() method to check whether two given vertices are connected by an edge or not.
6.	In class Graph, define print_adj_matrix() method to print adjacency matrix.
"""

class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_matrix = [[0] * vertex_count for i in range(vertex_count)]
    
    def add_edge(self, u, v, weight = 1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid Vertex")

    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str, row_list)))



g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(1, 2, 3)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 5)

print("Adjacency Matrix:")
g.print_adj_matrix()

print("Does an edge exist between 1 and 2?", g.has_edge(1, 2))

g.remove_edge(1, 2)

print("Does an edge exist between 1 and 2 after removal?", g.has_edge(1, 2))

print("Updated Adjacency Matrix:")
g.print_adj_matrix()