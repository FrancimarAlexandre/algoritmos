grafo = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'D': 3},
    'D': {}
}
def floyd_warshall(grafo):
    # Passo 1: mapear nós para índices
    vertices = list(grafo.keys())
    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}

    # Passo 2: criar matriz de distâncias
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    # Distância para si mesmo = 0
    for v in vertices:
        dist[index[v]][index[v]] = 0

    # Preencher com as arestas do grafo
    for u in grafo:
        for v, peso in grafo[u].items():
            dist[index[u]][index[v]] = peso

    # Passo 3: algoritmo Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Passo 4: converter matriz para dicionário organizado
    resultado = {}
    for i, u in enumerate(vertices):
        resultado[u] = {}
        for j, v in enumerate(vertices):
            resultado[u][v] = dist[i][j]

    return resultado


print(floyd_warshall(grafo))