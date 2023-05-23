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

# Contoh penggunaan algoritma Dijkstra
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4, 'E': 2},
    'C': {'B': 8, 'E': 7},
    'D': {'F': 2},
    'E': {'D': 6, 'F': 1},
    'F': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

for node, distance in distances.items():
    print(f"Jarak terpendek dari {start_node} ke {node} adalah {distance}")
