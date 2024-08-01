import heapq


def dijkstra(graph, start):
    # Initialize distances from the start vertex to all other vertices
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Min-heap (priority queue) to store vertices to process
    priority_queue = [(0, start)]

    while priority_queue:
        # Extract the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If a longer distance is found than the one already recorded,
        # continue (may happen due to duplicates in the heap)
        if current_distance > distances[current_vertex]:
            continue

        # Check neighboring vertices
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main():
    # Example graph represented as an adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    # Execute Dijkstra's algorithm
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)

    # Print the shortest paths from the start vertex
    for vertex, distance in shortest_paths.items():
        print(f"Shortest path from {start_vertex} to {vertex} is {distance}")


if __name__ == "__main__":
    main()
