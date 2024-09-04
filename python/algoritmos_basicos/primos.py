def primosI(n):
    l = []
    for i in range(1,n + 1):
        if n % i == 0:
            l.append(i)
    
    if len(l) > 2:
        print(f"o número {n} não é primo, ele é divisivel por : {l}")
    else:
        print(f"o número {n}  é primo, ele é divisivel por : {l}")



primosI(856)