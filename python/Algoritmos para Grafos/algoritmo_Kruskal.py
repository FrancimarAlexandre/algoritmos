arestas = [
    (1, 0, 1),
    (4, 1, 2),
    (3, 0, 2)
]

class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, x, y):
        raizX = self.find(x)
        raizY = self.find(y)

        if raizX == raizY:
            return False

        if self.rank[raizX] < self.rank[raizY]:
            self.pai[raizX] = raizY
        elif self.rank[raizX] > self.rank[raizY]:
            self.pai[raizY] = raizX
        else:
            self.pai[raizY] = raizX
            self.rank[raizX] += 1
        return True


def kruskal(arestas, num_vertices):
    uf = UnionFind(num_vertices)
    mst = []

    arestas_ordenadas = sorted(arestas)

    for peso, u, v in arestas_ordenadas:
        if uf.union(u, v):
            mst.append((u, v, peso))

    return mst
print(kruskal(arestas,3))