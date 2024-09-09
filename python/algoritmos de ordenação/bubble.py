vetor = [94,98,81,71,73,68,4,69,62,12]

def bubble_sort(val):
    compr = len(val) # comprimento do vertor

    for i in range(compr):
        for j in range(compr - i - 1):
            if val[j] > val[j + 1]:
                temp = val[j]
                val[j] = val[j + 1]
                val[j+1] = temp
    
print(f"lista original: {vetor}")
print()
bubble_sort(vetor)
print(f"Lista ordenada pelo bubble sorte: {vetor}")