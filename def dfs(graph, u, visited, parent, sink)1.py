def dfs(graph, u, visited, parent, sink):
    # Implementasi algoritma Depth-First Search
    visited[u] = True
    for v, capacity in enumerate(graph[u]):
        if not visited[v] and capacity > 0:
            parent[v] = u
            if v == sink:
                return True
            if dfs(graph, v, visited, parent, sink):
                return True
    return False


def ford_fulkerson(graph, source, sink):
    # Inisialisasi variabel
    max_flow = 0
    parent = [-1] * len(graph)

    # Jalankan algoritma Ford-Fulkerson
    while dfs(graph, source, [False] * len(graph), parent, sink):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


# Contoh penggunaan algoritma Ford-Fulkerson
graph = [
    [0, 10, 10, 0, 0, 0, 0, 0],
    [0, 0, 2, 4, 8, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 0, 0, 0, 0, 10, 0],
    [0, 0, 0, 0, 0, 0, 10, 0],
    [0, 0, 0, 0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
source = 0
sink = 7
max_flow = ford_fulkerson(graph, source, sink)
print(f'Aliran maksimum adalah {max_flow}')
