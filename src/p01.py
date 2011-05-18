def p1():
    print sum(x for x in range(1000) if not (x%5 and x%3))
p1()
