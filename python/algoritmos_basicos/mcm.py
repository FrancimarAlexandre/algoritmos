#  Mínimo Comum Múltiplo (MCM) Recursivo

def mcmR(n, m, i=1):
    if (n * i) % m == 0:
        return n * i
    return mcmR(n, m, i + 1)

print(mcmR(2, 12))
#  Mínimo Comum Múltiplo (MCM) Iterativo
def mcmI(n,m, i = 1):
    while True:
        if (n * i) % m == 0:
            return n * i
        i += 1

print(mcmI(32, 13))