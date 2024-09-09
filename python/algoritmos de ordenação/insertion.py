vetor = [94,98,81,71,73,68,4,69,62,12]

def insertion_sort(val):
    compr = len(val)
    for i in range(1,compr):
        index = val[i]
        j = i
        while j > 0 and index < val[j-1]:
            val[j] = val[j-1]
            j -=1
        val[j] = index

print(f"lista original: {vetor}")
print()
insertion_sort(vetor)
print(f"Lista ordenada pelo insertion sorte: {vetor}")