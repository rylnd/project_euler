def prob18():
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    trian_in = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.split('\n')

    matr = [trian_in[k].split() for k in range(15)]
    def printt():
        for k in range(15):
            for j in matr[k]:
                print j,
            print '\n',

    def color(n):
        for k in range(15):
            for j in matr[k]:
                if int(j) <= n:
                   matr[k][matr[k].index(j)] = FAIL + j + ENDC
                


    def best(n):
        total = 75
        indx = 0
        for i in range(1, 15):
            if int(matr[i][indx]) <=n:
                total = total + int(matr[i][indx+1])
                indx +=1
            elif int(matr[i][indx+1])<=n:
                total = total + int(matr[i][indx])
            else:
                indx = matr[i].index(max(matr[i][indx], matr[i][indx+1]))
                total = total + int(matr[i][indx])
        return total
    
    for j in range(100):
        print "<=%d: %d" %(j, best(j))

    def smrt():
        for j in range(13, 0, -1):
            for k in matr[j]:
                indx = matr[j].index(k)
                matr[j][indx] = int(matr[j][indx]) + max(int(matr[j][indx]), int(matr[j][indx+1]))



    smrt()

    printt()
    color(15)
    printt()

prob18()
