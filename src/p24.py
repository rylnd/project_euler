from sys import exit
def prob24():
    tmp = ""
    global countt
    countt = 0
    def recur_24(tmp, rng):
        global countt
        if countt==999999:
            num, new = "0123456789", ["-" for i in range(10)]
            for index, char in enumerate(tmp):
                new[9-int(char)] = index
            print "tmp: %s\tnew: %s" %(tmp, new)
            exit(0)
            return
        for i in range(rng+1):
            if rng==10:
                countt +=1
                print "tmp: %s\trng: %d\tcnt: %d" %(tmp, rng, countt)
                return
            recur_24(tmp + str(i), rng+1)

    recur_24("", 0)

prob24()


    
