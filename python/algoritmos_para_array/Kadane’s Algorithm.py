def maxSubarraySum(array):
    res = array[0]

    for i in range(len(array)):
        currSum = 0
        for j in range(i, len(array)):
            currSum = currSum + array[j]
            res = max(res, currSum)
    return res


array = [2, 3, -8, 7, -1, 2, 3]
print(maxSubarraySum(array))