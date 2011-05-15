def req34(num_p):
    sum,tmp = 0,str(num_p)
    for char in tmp:
        sum+=fact(int(char))
    return sum==num_p


def fact(n):
        ret = 1
        while(n >=1):
            ret *= n
            n -= 1
        return ret
i = 1
while(1):
    if(req34(i)):print i
    i+=1
