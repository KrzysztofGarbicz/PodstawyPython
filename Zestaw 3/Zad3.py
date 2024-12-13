import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Przykład
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3), ('E', 8)],
    'D': [('B', 10), ('C', 3), ('E', 2)],
    'E': [('C', 8), ('D', 2)]
}


start_vertex = 'A' # Start
shortest_paths = dijkstra(graph, start_vertex)

print(f"Najkrótsze ścieżki od wierzchołka {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"{vertex}: {distance}")
