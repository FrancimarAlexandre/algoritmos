
def rotacionar_array(array,k):
    return array[-k:] + array[:-k]

array = [1,2,3,4,5,6,7,8]

print(rotacionar_array(array,1))