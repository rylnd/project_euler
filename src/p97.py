def solve(a,b,c,m):
    return (c* pow(a,b,10**m) +1) % 10**m
print solve(2,7830457,28433,10)
