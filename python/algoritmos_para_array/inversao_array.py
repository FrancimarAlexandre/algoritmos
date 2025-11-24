def inverter_array(array):
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    return array

array = [1,2,3,4,5]
print(inverter_array(array))