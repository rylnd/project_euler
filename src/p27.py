def calc(n,a,b):
    return n**2 + a*n + b

def primes(n):
    if n==2: return [2]
    elif n<2: return []
    s = range(3, n+1, 2)
    mroot = n ** 0.5
    half = (n+1)/2-1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m*m-3)/2
            s[j] = 0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2] + [x for x in s if x]




prime = primes(1000000)
alle = {}
max_=0
for i in range(-999, 1000, 2):
    for j in range(-999, 1000, 2):
        n = 0
        while(calc(n,i,j) in prime):
            n +=1
        alle[i*j] = n
        if n > max_:
            max_=n
            print "i*j:%d, n: %d"%(i*j,n)
            
    
print max(alle, key=alle.get)


