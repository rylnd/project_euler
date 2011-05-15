def makeset(n):
    l,tmp = [],str(n)
    for char in tmp:
        l.append(char)
    return set(l)

n = 0
while(True):
    n+=1
    if(makeset(2*n)==makeset(3*n)==makeset(4*n)==makeset(5*n)==makeset(6*n)):
        print n
        break

    
