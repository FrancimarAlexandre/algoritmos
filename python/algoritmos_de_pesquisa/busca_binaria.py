def busca_binaria_iterativo(lista, item):
    low = 0
    high = len(lista) - 1
    while low <= high:
        meio = (low + high) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] < item:
            low = meio + 1
        elif lista[meio] > item:
            high = meio - 1
    return -1


def busca_binaria_recursivo(lista, item, low, high):
    if low > high:
        return -1
    meio = low + (high - low) // 2
    if lista[meio] == item:
        return meio
    elif lista[meio] < item:
        return busca_binaria_recursivo(lista, item, meio + 1, high)
    elif lista[meio] > item:
        return busca_binaria_recursivo(lista, item, low, meio - 1)


lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
item = 56
low = 0
high = len(lista) - 1

print("testando busca binária iterivo")
print(busca_binaria_iterativo(lista, item))

print("\n")

print("testando busca binária recursivo")
print(busca_binaria_recursivo(lista, item, low, high))
