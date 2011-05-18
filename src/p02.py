sum2 = 0
def p2():
    def fib(x, y, z):
        if x <= 4000000 and y <= 4000000:
            new = x + y
            if new%2==0:
                global sum2
                sum2 += new
            z += 1
	    fib(y, new, z)
    fib(0, 1, 1)
    print sum2

p2()
    
    
    
