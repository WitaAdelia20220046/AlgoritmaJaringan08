class Edge:
    def __init__(self, v, capacity, reverse_edge):
        self.v = v
        self.capacity = capacity
        self.flow = 0
        self.reverse_edge = reverse_edge


def add_edge(graph, u, v, capacity):
    forward_edge = Edge(v, capacity, None)
    reverse_edge = Edge(u, 0, forward_edge)
    forward_edge.reverse_edge = reverse_edge

    graph[u].append(forward_edge)
    graph[v].append(reverse_edge)


def dfs(graph, u, sink, visited, path_flow):
    visited[u] = True

    if u == sink:
        return True

    for edge in graph[u]:
        v = edge.v
        residual_capacity = edge.capacity - edge.flow

        if not visited[v] and residual_capacity > 0:
            min_flow = min(path_flow, residual_capacity)

            if dfs(graph, v, sink, visited, min_flow):
                edge.flow += min_flow
                edge.reverse_edge.flow -= min_flow
                return True

    return False


def ford_fulkerson(graph, source, sink):
    max_flow = 0

    while True:
        visited = [False] * len(graph)
        path_flow = float('inf')
        if not dfs(graph, source, sink, visited, path_flow):
            break

        max_flow += path_flow

    return max_flow


# Contoh penggunaan algoritma Ford-Fulkerson pada jaringan telekomunikasi
graph = [[] for _ in range(6)]  # Inisialisasi graf dengan 6 node

# Menambahkan edge dan kapasitas antar node
add_edge(graph, 0, 1, 10)
add_edge(graph, 0, 2, 10)
add_edge(graph, 1, 2, 2)
add_edge(graph, 1, 3, 4)
add_edge(graph, 1, 4, 8)
add_edge(graph, 2, 4, 9)
add_edge(graph, 3, 5, 10)
add_edge(graph, 4, 5, 10)

source = 0
sink = 5

max_flow = ford_fulkerson(graph, source, sink)
print(f"Aliran maksimum dalam jaringan telekomunikasi adalah {max_flow}")
