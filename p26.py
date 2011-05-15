def long_div(div):
    count,quot,rem, = 0, 1/div, 1%div
    seen_rems = []
    fin = str(quot)+"."
    while(quot==0): #until we get to a real num
        rem *=10 #drop down
        quot,rem = rem/div, rem%div
        fin += str(quot)

    while(True):
        count +=1
        rem *=10 #drop down
        quot,rem = rem/div, rem%div
        if(rem in seen_rems):
            break
        elif rem==0:
            count = 0
            break
        else:
            seen_rems.append(rem)
        fin += str(quot)
        

#    return fin,count-1, seen_rems
    return count

fin_list = dict([(i,long_div(i)) for i in range(1,1000)])

print max(fin_list, key=fin_list.get)


