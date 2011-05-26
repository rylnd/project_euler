def p28():
    tot, cntr, inc = 1,1,2
    for layer in range(500):
        for i in range(4):    #one square
            #print cntr
            cntr += inc
            tot += cntr
        inc += 2

    #print cntr
    print tot
p28()
