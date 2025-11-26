arestas = [
    (0, 1, 1),
    (1, 2, 4),
    (0, 2, 3)
]

def bellman_ford(arestas, num_vertices, origem):
    dist = [float('inf')] * num_vertices
    dist[origem] = 0

    # Relaxamento
    for _ in range(num_vertices - 1):
        atualizado = False
        for u, v, peso in arestas:
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                atualizado = True
        if not atualizado:
            break

    # Detectar ciclo negativo
    for u, v, peso in arestas:
        if dist[u] + peso < dist[v]:
            raise Exception("Ciclo negativo detectado no grafo!")

    return dist

print(bellman_ford(arestas, 3, 2))
