def prob14():
    def start(n, mx):
        tmp = 0
        print "start: %d" %n
        while n!=1:
            if(n%2==0):
                n = n / 2
                tmp=tmp+1
                if(tmp > mx):
                    mx = tmp
                    print "\tMAX"
            else:
                n = 3*n + 1
                tmp=tmp+1
                if(tmp > mx):
                    mx = tmp
                    print "\tMAX"
        return mx

    q = 0
    for j in range(0, 1000000):
        q = start(j, q)
        print q+1
    print "MAX: %D" %(q+1)



prob14()
