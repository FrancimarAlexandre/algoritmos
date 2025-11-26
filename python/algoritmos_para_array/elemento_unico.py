def elemento_unico(array):
    elementos_unicos = []
    unico = set(array)

    for valor in unico:
        elementos_unicos.append(valor)
    return elementos_unicos

array = [1,1,2,2,3,4,4,5,8,7,5,6]

print(elemento_unico(array))