def prob21():
    def amic(n):
        return sum(x for x in range(1, n) if n%x==0)

 
    tot = sum(x for x in range(1, 10000) if amic(amic(x))==x and amic(x)!=x)
        
