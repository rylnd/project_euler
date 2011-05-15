def is_pal(pal):
    if str(pal)[0]=='0': return False
    pal_s, len_s = str(pal), len(str(pal))
    for i in range(len_s/2):
#        print "[%d][%d]"%(i, len_s-i-1)
        if(not pal_s[i]==pal_s[len_s-i-1]):
            return False
    return True

        
def to_bin(dec):
    '''returns a string representation of the given decimal number in binary'''
    return bin(dec)[2:len(bin(dec))]


def both(dec):
    return is_pal(dec) and is_pal(to_bin(dec))


fin = [x for x in range(1000000) if both(x)]
print fin
print sum(fin)



