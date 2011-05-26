def p31():
    pence = 200
    denoms = [200,100,50,20,10,5,2,1]
    names = {200:"200p", 100:"200p", 50:"50p", 20:"20p", 10:"10p", 5:"5p", 2:"2p", 1:"1p"}
    def count_combs(left, i, comb, add): #denom[i] is largest denom
        if add: comb.append(add) 
        if left==0 or (i+1)==len(denoms): #if done filling or i is 1p
            if(i+1)==len(denoms) and left>0: #if we have some total to fill
                comb.append((left, denoms[i])) #fill rest with 1ps
                i +=1
            while i < len(denoms): #while current denom isn't 1p
                comb.append((0,denoms[i])) #fill comb with 0s
                i+=1
    #        print " ".join("%d %s" % (n,names[c]) for (n,c) in comb) #print comb
            return 1
        cur = denoms[i] #cur = largest denom
        return sum(count_combs(left-x*cur, i+1, comb[:], (x,cur)) for x in range(0,int(left/cur)+1))
    
    print count_combs(pence, 0, [], None)

p31()
