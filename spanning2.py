
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1},
    'C': {'A': 3, 'B': 1}
}

start_node = 'A'

# Panggil fungsi minimum_spanning_tree
mst_edges, mst_cost = minimum_spanning_tree(graph, start_node)

# Tampilkan hasil
print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(edge)
print("Total Cost:", mst_cost)
