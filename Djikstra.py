import heapq

def dijkstra(graph, start):
    # Initialize distances from start node to all other nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store nodes to be visited, with the start node having distance 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If current node is already visited with a shorter distance, skip it
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    # Take user input for graph
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = input("Enter edge and weight (start end weight): ").split()
        weight = int(weight)
        if u not in graph:
            graph[u] = {}
        graph[u][v] = weight

    start_node = input("Enter start node: ")
    shortest_distances = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node)
    for node, distance in shortest_distances.items():
        print("To node", node, ":", distance)

if __name__ == "__main__":
    main()
