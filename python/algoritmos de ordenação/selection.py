vetor = [94,98,81,71,73,68,4,69,62,12]

def selection_sort(val):
    compr = len(val) # comprimento do vertor
    for i in range(0,compr):
        min_index = i
        for j in range(i + 1, compr):
            if val[j]< val[min_index]:
                min_index = j
        val[i],val[min_index] = val[min_index],val[i]

print(f"lista original: {vetor}")
print()
selection_sort(vetor)
print(f"Lista ordenada pelo selection sorte: {vetor}")