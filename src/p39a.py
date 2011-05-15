
def satisfies(a,b,c,p):
    if (a*a + b*b == c*c) and a+b+c==p:
        return 1
    return 0

def total(p):
    a,b,c,tot = 1,1,p-2,0
    

    

l = []
for i in range(3,1001):
    l.append((i,total(i)))


print l,max(l)

def getabc(m,n):
    a = m**2 -n**2
    b = 2*m*n
    c = m**2 + n**2
    return a,b,c
