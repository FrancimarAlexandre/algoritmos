def intersecao_arrays(array1, array2):
    intersecao = []
    for elemento in array1:
        if elemento in array2 and elemento not in intersecao:
            intersecao.append(elemento)
    return intersecao


# Exemplo de uso
a1 = [1, 2, 3, 4, 5, 5]
a2 = [4, 5, 6, 7]

print(intersecao_arrays(a1, a2))
