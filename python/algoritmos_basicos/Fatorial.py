# fatorial recursivo

def fatRec(n):
    if n == 1 or n ==0:
        return 1
    return fatRec(n-1) * n

print(fatRec(15))

def fatInter(n):
    result = 1

    for i in range(1,n+1):
        result *= i

    return result

print(fatInter(15))