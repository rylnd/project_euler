#!/usr/bin/python

def lychrel(n, it):
    if it<50:
        rev = n[::-1]
        _sum = str(int(n) + int(rev))
        if _sum==_sum[::-1]:
            return int(_sum)
        else: return lychrel(_sum, it+1)
    else: return 0

l = [x for x in range(1,10000) if not lychrel(str(x),0)]
print len(l)




    
    
