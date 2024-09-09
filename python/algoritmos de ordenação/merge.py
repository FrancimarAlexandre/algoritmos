vetor = [94,98,81,71,73,68,4,69,62,12]

def merge_sort(val):
    compr = len(val) # comprimento do vertor
    if compr <= 1:
        return val
    min_index = compr // 2
    val_left = val[:min_index]
    val_right = val[min_index:]

    sortedLeft = merge_sort(val_left)
    sortedRight = merge_sort(val_right)

    return merge(sortedLeft,sortedRight)

def merge(left,right):
    result = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


print(f"lista original: {vetor}")
print()
vetor_ord = merge_sort(vetor)
print(f"Lista ordenada pelo merge sorte: {vetor_ord}")