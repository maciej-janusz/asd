#O(VlogV+E)
import heapq

def prim(graph, start=0):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, start, -1)]
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, u, from_node = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += weight
        if from_node != -1:
            mst_edges.append((from_node, u, weight))

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return total_cost, mst_edges
