def p17():
    ones = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": ""
        }
    def thousands(_n):
        return "onethousand"

    def hundreds(_n):
        hnd = ones.get(_n[0],"")
        rst = _n[1:3]
        return ("" if hnd is "" else hnd + "hundred") + ("and"+tens(rst) if int(rst)>0 else "")
    def tens(_n):

        if int(_n)<20:
            return teens(_n)
        else:
            digs = {
                "2": "twenty",
                "3": "thirty",
                "4": "forty",
                "5": "fifty",
                "6": "sixty",
                "7": "seventy",
                "8": "eighty",
                "9": "ninety",
                "0": ""
                }
            return digs.get(_n[0], "") + ones.get(_n[1:2],"")
    def teens(_n):

        digs = {
            "0": "",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
            "10": "ten",
            "11": "eleven",
            "12": "twelve",
            "13": "thirteen",
            "14": "fourteen",
            "15": "fifteen",
            "16": "sixteen",
            "17": "seventeen",
            "18": "eighteen",
            "19": "nineteen",
            "00": "",
            "01": "one",
            "02": "two",
            "03": "three",
            "04": "four",
            "05": "five",
            "06": "six",
            "07": "seven",
            "08": "eight",
            "09": "nine"
            }
        
        return digs.get(_n, "")


    while (1):
        _n = raw_input("enter a number:")
        
        choo = {
            4: thousands, 3: hundreds,
            2: tens, 1: teens
            }
        
            
        result = [choo[len(str(i))](str(i)) for i in range(1001)]
        print result
        l =  reduce(lambda x,y: x+y, result)

        print l
        print len(l)


        #loop
        '''for i in range(500):
            f = choo[len(str(i))]
            print f(str(i))'''

        f = choo[len(_n)]
        print f(_n)

p17()
