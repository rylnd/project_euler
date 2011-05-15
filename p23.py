def prob23():
    def abun(n):
        return sum(x for x in range(1, n) if n%x==0)
    #have all the abundants we need
    abun = [x for x in range(28123) if abun(x)>x]
    #get all possible sums
    sums = set(x+y for x in abun for y in abun)
#    print sums
    final_set = [x for x in range(28123) if x not in sums]
    print final_set
    print sum(final_set)
    
    

prob23()
        
