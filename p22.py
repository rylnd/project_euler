def prob22():
    def val(n):
        return ord(n)-64

    names = sorted(open('names.txt').next().split(','))
    names = map(lambda x: x.strip('"\n'), names)
    
    print sum((names.index(name)+1 )* sum(val(n) for n in name) for name in names)
    

prob22()


