def p21():
    #define amicable to simplify the iffs
    def amic(n):
        return sum(x for x in range(1, n) if not n%x)
    #sum all amicable pairs under 10,000
    tot = sum(x for x in range(1, 10000) if amic(amic(x))==x and amic(x)!=x)

    print tot

p21()
        
