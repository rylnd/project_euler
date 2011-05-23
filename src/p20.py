def p20():
    tot = 0
    #get 100!
    _sum = str(reduce(lambda x,y: x*y, range(2,100)))
    #convert to string to allow indexing
    _sum = str(_sum)

    # sum over digits
    tot = sum(int(x) for x in _sum)
    print tot

p20()
