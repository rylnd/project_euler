def primes(n):
    '''returns all primes less than n'''
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

def rotate(string):
    l,tmp,length = [], string, len(string)
    for i in range(length):
        l.append(string[i:]+string[:i])
    return l

prime = primes(1000000)
for ev in ('2', '4', '5', '6', '8'):
    prime = [x for x in prime if not ev in str(x)]

print prime
circ_primes = []
for x in prime:
    add = True
    for s in rotate(str(x)):
        add = add & (int(s) in prime)
    if(add):
        circ_primes.append(x)


