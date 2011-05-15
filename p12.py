import os
def prob12():
    def triangle(count):
        tmp = 0
        for i in range(1, count):
            tmp = tmp + (i)
            factors(tmp)
        return tmp


    def factors(num):
#        print num
        count = 0
        for i in range(1, num):
            if(num%i==0):
                count=count+1
                if(count>500):
                    print "FOUND: %d, count %d" %(num, count)
                    os._exit(0)
#                print "\t %d\n" %(i)
 
            
        print "num: %d\tcount:%d" %(num, count)

    triangle(36215980)
#    triangle(50000000)
    

prob12()

