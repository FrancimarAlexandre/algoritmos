grafo = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'D': 3},
    'D': {}
}

import heapq

def dijkstra(grafo, origem):
    dist = {v: float('inf') for v in grafo}
    dist[origem] = 0

    fila = [(0, origem)]  # (distância, nó)

    while fila:
        distancia_atual, atual = heapq.heappop(fila)

        if distancia_atual > dist[atual]:
            continue

        for vizinho, peso in grafo[atual].items():
            nova_dist = distancia_atual + peso

            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                heapq.heappush(fila, (nova_dist, vizinho))

    return dist


print(dijkstra(grafo,'B'))