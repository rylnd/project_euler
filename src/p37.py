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

def only(p):
    sp = str(p)
    bad = ['4','6','8'] 
    for num in bad:
        if num in sp: return 0
    if sp[0]=='9' or sp[-1]=='9' or sp[0]=='1' or sp[-1]=='1':return 0
    if '2' in sp[1:] or '5' in sp[1:]:return 0
    return True

prime = primes(1000000)
prime2 = filter(only,prime)


def istrunc(p):
    sp = str(p)
    for i in range(1,len(sp)):
        if int(sp[:0-i]) not in prime or int(sp[i:]) not in prime:
            return 0
    return True

tot=[]
for p in prime2[4:]:
    if istrunc(p):
        tot.append(p)
        if len(tot)>=11:
            break

print tot, sum(tot)
