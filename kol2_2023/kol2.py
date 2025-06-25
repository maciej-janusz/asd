from kol2testy import runtests

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            if self.rank[u_root] > self.rank[v_root]:
                self.parent[v_root] = u_root
            elif self.rank[u_root] < self.rank[v_root]:
                self.parent[u_root] = v_root
            else:
                self.parent[v_root] = u_root
                self.rank[u_root] += 1
            return True
        return False

def kruskal(edges, V, E):
    edges = sorted(edges, key=lambda x: x[2])

    for i in range(E):
        uf = UnionFind(V)
        cost = 0
        cnt = 0
        for j in range(i, E):
            u, v, w = edges[j]
            if uf.union(u, v):
                cost += w
                cnt += 1
                if cnt == V - 1:
                    return cost
            else:
                break

    return None
def beautree(G):
    V = len(G)
    edges = []
    for u in range(V):
        for v, w in G[u]:
            if u < v:
                edges.append((u, v, w))
    E = len(edges)

    return kruskal(edges, V, E)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )