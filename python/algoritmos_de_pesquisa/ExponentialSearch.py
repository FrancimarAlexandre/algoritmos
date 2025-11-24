def exponential_search(array, key):
    size = len(array)

    if size == 0:
        return -1

    if array[0] == key:
        return 0

    m = 1
    while m < size and array[m] <= key:
        m *= 2

    low = m // 2
    high = min(m, size - 1)

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [2, 4, 7, 10, 14, 20, 25, 30]
key = 14

result = exponential_search(arr, key)
print("Índice encontrado:", result)
