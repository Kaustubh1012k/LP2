from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))

    def get_neighbors(self, v):
        return self.adjacency_list.get(v, [])

    def a_star_algorithm(self, start_node, stop_node, h_values):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n is None or g[v] + h_values[v] < g[n] + h_values[n]:
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist!')
        return None

def main():
    g = Graph()

    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        u, v = input("Enter edge (start end): ").split()
        weight = int(input("Enter weight: "))
        g.add_edge(u, v, weight)

    h_values = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for i in range(num_nodes):
        node, h_value = input("Enter node and its heuristic value (node h_value): ").split()
        h_values[node] = int(h_value)

    start_node = input("Enter start node: ")
    stop_node = input("Enter stop node: ")

    path = g.a_star_algorithm(start_node, stop_node, h_values)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
