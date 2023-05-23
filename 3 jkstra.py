import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# Contoh penggunaan algoritma Dijkstra untuk menentukan rute terpendek
graph = {
    'A': {'B': 10, 'C': 15},
    'B': {'D': 12, 'E': 15},
    'C': {'E': 10, 'F': 12},
    'D': {'G': 10},
    'E': {'G': 5, 'H': 8},
    'F': {'H': 5},
    'G': {'I': 15},
    'H': {'I': 10},
    'I': {}
}

start = 'A'
distances = dijkstra(graph, start)

print("Rute Terpendek dan Total Jarak:")
for node, distance in distances.items():
    if distance != float('inf'):
        print(f"{start} -> {node}: {distance}")
