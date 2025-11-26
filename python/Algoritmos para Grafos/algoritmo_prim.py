grafo = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3)],
    2: [(1, 3), (3, 8)],
    3: [(0, 6), (2, 8)]
}
import heapq

def prim(grafo, inicio=0):
    visitado = set()
    mst = []
    fila = [(0, inicio, None)]  # (peso, nó, pai)

    while fila:
        peso, atual, pai = heapq.heappop(fila)

        if atual in visitado:
            continue

        visitado.add(atual)

        if pai is not None:
            mst.append((pai, atual, peso))

        for vizinho, p in grafo[atual]:
            if vizinho not in visitado:
                heapq.heappush(fila, (p, vizinho, atual))

    return mst
print(prim(grafo))