##SEE http://blog.ry-land.com/?p=91 for details on this one.
import sys
def p12():
    def factor(n):  
        if n == 1: return [1]  
        i = 2  
        limit = n**0.5  
        while i <= limit:  
            if n % i == 0:  
                ret = factor(n/i)  
                ret.append(i)  
                return ret  
            i += 1  
            
        return [n]

    def factorexp(L):
        prime,count,list=0,0,[]
        for x in L:
            if x == prime:
                count += 1
            else:
                if prime != 0:
                    list = list + [str(count)]
                prime,count=x,1
        list = list + [str(count)]
        return list

    def numfactors(L):
        count=1
        for x in L:
            count = count * (int(x) +1)
        if count>500:
            print "\t %d\n" %count
            sys.exit(0)
        print "\t %d\n" %count
        return count

    def triangle(count):
        tmp = 0
        for i in range(1, count):
            tmp = tmp + (i)
            print tmp
            numfactors(factorexp(factor(tmp)))
        return tmp

    triangle(34000000) #arbitrarily large

p12()
