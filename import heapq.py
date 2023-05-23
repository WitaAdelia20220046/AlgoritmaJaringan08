import heapq

def minimum_spanning_tree(graph, start):
    # Inisialisasi variabel yang diperlukan
    visited = set([start])
    edges = [(cost, start, end) for end, cost in graph[start].items()]
    heapq.heapify(edges)
    mst_cost = 0
    mst_edges = []

    # Looping sampai semua simpul dikunjungi
    while edges:
        # Ambil simpul dengan bobot terkecil
        cost, start, end = heapq.heappop(edges)
        # Jika simpul tujuan belum dikunjungi
        if end not in visited:
            # Tambahkan simpul ke daftar simpul yang sudah dikunjungi
            visited.add(end)
            # Tambahkan jarak ke total biaya minimum
            mst_cost += cost
            # Tambahkan edge ke daftar MST
            mst_edges.append((start, end, cost))
            # Tambahkan edge dari simpul tujuan ke daftar edge
            for end_next, cost_next in graph[end].items():
                if end_next not in visited:
                    heapq.heappush(edges, (cost_next, end, end_next))

    # Kembalikan daftar edge dan total biaya minimum
    return mst_edges, mst_cost
