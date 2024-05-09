class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

def kruskals_algorithm(graph):
    mst = []
    vertex_index_map = {}  # Map vertex labels to integer indices
    disjoint_set = DisjointSet(len(graph))
    edges = []

    # Assign integer indices to each vertex label
    index = 0
    for u in graph.keys():
        vertex_index_map[u] = index
        index += 1

    for u, adj_list in graph.items():
        for v, weight in adj_list:
            edges.append((weight, u, v))

    edges.sort()

    for weight, u, v in edges:
        u_index = vertex_index_map[u]  # Map vertex labels to integer indices
        v_index = vertex_index_map[v]
        if disjoint_set.find(u_index) != disjoint_set.find(v_index):
            mst.append((u, v, weight))
            disjoint_set.union(u_index, v_index)

    return mst

def get_graph_input():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = input("Enter edge (source destination cost): ").split()
        weight = int(weight)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # Assuming undirected graph
    return graph

def main():
    graph = get_graph_input()
    mst = kruskals_algorithm(graph)
    print("Minimum Spanning Tree (Kruskal's Algorithm):")
    for edge in mst:
        print(edge)

if __name__ == "__main__":
    main()
