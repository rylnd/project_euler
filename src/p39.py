#!/usr/bin/python
from fractions import gcd

#Euclid's Formula
def getabc(m,n):
    a = m**2 -n**2
    b = 2*m*n
    c = m**2 + n**2
    return a,b,c

#calculate all PPTs for which p < 1000
prim_trips = [getabc(m,n) for m in range(1,100) for n in range(1,100) if m>n and gcd(m,n)==1 and 2*m*m + 2*m*n<=1000 and (m%2==0 or n%2==0)]

#find all possible triples for a given p
def total(p):
    return sum([1 for (a,b,c) in prim_trips if p%(a+b+c)==0])

#collect all possible solutions for each perimeter p
totals = [(p,total(p)) for p in range(1,1001)]

#get max
print max(totals, key=lambda x: x[1] )
