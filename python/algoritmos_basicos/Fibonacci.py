# Fibonacci recursivo

def fibR(n):
    if n == 0:
        return 0
    if n== 1 or n == 2:
        return 1
    return fibR(n-1) + fibR(n-2)

print(fibR(35))

# Fibonacci Intaretiva

def fibI(n):
    if n == 0:
         return 0
    elif n == 1 or n==2:
         return 1
    a,b = 0,1
    for _ in range(2,n+1):
        a,b = b,a+b
    return b
print(fibI(35))
