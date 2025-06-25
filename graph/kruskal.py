#O(ElogE)
from union_find import UnionFind

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst = []
    mst_cost = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            mst_cost += weight
        if len(mst) == n - 1:
            break

    return mst, mst_cost
