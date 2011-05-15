from __future__ import division
def fact(n):
    if n==0 or n==1: return 1
    else:
        return reduce(lambda x,y: x*y, range(1,n+1))

def comb(n,r): return fact(n) / (fact(r)*fact(n-r))

print sum([1 for n in range(1,101) for r in range(1, n+1) if comb(n,r)>=1000000])
