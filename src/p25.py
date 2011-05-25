def fib():
    a,b,i = 1,1,1
    while 1:
        yield a,i
        a,b,i = b,a+b, i+1

def p25():
    for f, i in fib():
        if len(str(f))==1000:
            break
    print i

p25()
