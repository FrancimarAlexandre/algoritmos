vetor = [94,98,81,71,73,68,4,69,62,12]

def partition(val,low,high):
    pivot = val[high]
    i = low -1
    for j in range(low,high):
        if val[j] <= pivot:
            i += 1
            val[i],val[j] = val[j],val[i]
    val[i+1],val[high] = val=high,val[i+1]

    return i + 1
   
def quick_sort(val,low = 0,high = None):
    if high is None:
        high = len(val) - 1
    
    if low < high:
        pivot_index = partition(val,low,high)
        quick_sort(val,low,pivot_index-1)
        quick_sort(val,pivot_index+1,high)


print(f"lista original: {vetor}")
print()
quick_sort(vetor)
print(f"Lista ordenada pelo quick sorte: {vetor}")