# máximo divisor comum Resursivo

def mdcR(n,m):
    if m == n:
        return n
    resto = n % m
    n = m
    n = resto
    return mdcR(n,n%m) 

print(mdcR(75,30))