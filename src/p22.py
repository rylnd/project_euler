def p22():
    #gets int out of char representation
    def val(n):
        return ord(n)-64

    #get list of names, split on commas
    names = sorted(open('names.txt').next().split(','))

    #bad input, remove newlines :(
    names = map(lambda x: x.strip('"\n'), names)

    #sum scores based on their indices in the list * values for each char in the name
    print sum((names.index(name)+1 )* sum(val(n) for n in name) for name in names)
    

p22()


