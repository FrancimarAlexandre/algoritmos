# máximo divisor comum Rescursivo

def mdcR(n,m):
    if not m:
        return n
    return mdcR(m,n%m) 

print(mdcR(75,30))

# máximo divisor comum iterativo

def mdcI(n,m):
    while m:
        n,m = m,n%m
    return n

print(mdcI(75,30))