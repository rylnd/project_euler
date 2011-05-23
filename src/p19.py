def p19():

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_cnt, suns, year = 2, 0, 1901
    for i in range(1,101):
        year += i
        if year%4==0: days[1]=29
        else: days[1]=28
        for day in days:
            day_cnt +=day
            if day_cnt%7==0:
                suns +=1

    print "total days: %d \ntotal suns: %d" %(day_cnt, suns)
        

                    

p19()
