# http://blog.ry-land.com/?p=91 for a good deal of detail on this one
def p24():
    def fact_to_perm(n):
            '''takes a factoradic and returns the permutation it represents '''
            ret = ""
            lst = range(len(str(n)))
            for char in str(n):
                found = lst[int(char)]
                lst.remove(found)
                ret += str(found)
            return ret
    
    
    def to_perm(_fct):
            '''takes a factoradic and returns the decimal number it represents.
            this number x is also the place in which the permutation represented by this factoradic occurs when these permuations are listed in lexicographic order. neat!
            '''
            return sum(int(char)*fact(len(_fct)-ind-1) 
                       for ind,char in enumerate(_fct))
    
    def fact(n):
            ret = 1
            while(n >=1):
                ret *= n
                n -= 1
            return ret
        
    def dec_to_fact(n,k):
            '''takes a decimal n and returns the factoradic representation
            of that number given permutations of nums in range(k)'''
    
            ret, tot, left = [],0, n
            for i in range(k-1, -1, -1):
                added = False
                for j in range(i+1):
                    if j * fact(i)>left:
                        ret.append(j-1)
                        left -= (j-1)*fact(i)
                        added = True
                        break
                if(not added):
                    ret.append(j)
                    left -= j*fact(i)
            return ret
    
    print dec_to_fact(999999, 10)

p24()
