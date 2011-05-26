def p27():
    prod, best = 41, 40
    def isprime(x):
        if x<2: return 0
        if x%2:
            for i in range(3,int(x**0.5),2):
                if not x%i: return 0
        else: return 0
        return 1

    for a in range(-999, 1000):
        for b in range(1000):
            c=0
            while isprime(c**2 + a*c + b)==1:
                c+=1
            if c>best:
                best, prod = c, a*b
    print prod

p27()
