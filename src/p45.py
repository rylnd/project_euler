def tri(n):
    l = []
    for i in range(1,n+1):
        l.append(i*(i+1)/2)
    return set(l)

def pent(n):
    l = []
    for i in range(1,n+1):
        l.append(i*(3*i-1)/2)
    return set(l)

def hex(n):
    l = []
    for i in range(1,n+1):
        l.append(i*(2*i-1))
    return set(l)

hex_ = hex(400000)
pen_ = pent(400000)
tri_= tri(400000)

print hex_ & pen_ & tri_
#l = [x for x in range(2000000, 4000000) if x in hex if x in pen if x in tri]
#print l
