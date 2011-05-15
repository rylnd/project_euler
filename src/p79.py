#!/usr/bin/python
class digit:
    def __init__(self,x):
        self.dig = x
        self.left = set()
        self.right = set()

#split the input into a list of 3-digit login attempts
logins = list(set([l.strip('\n\r') for l in open('keylog.txt')]))

#compile key's left and right sets
def place(key):
    num = str(key.dig) 
    check = [line for line in logins if num in line]
    for line in check: #for each line that contains this digit
        place = line.index(num)
        for i in line:
            if line.index(i) < place:
                key.left.add(i)
            elif line.index(i) >place:
                key.right.add(i)

#create an instance for each digit present
obs = [digit(l) for l in ['0','1','2','3','6','7','8','9']]
#create those instances' associated sets
[place(dig) for dig in obs]

#place in logical order
obs.sort(key=lambda x: x.left)
print ''.join([d.dig for d in obs])
print reduce(lambda x,y: x+y,[d.dig for d in obs])



''' 
SORT V0
for i in range(9):
    for dig in obs:
        if len(dig.left)==i:
            print dig.dig
SORT V1
print [dig.dig for i in range(9) for dig in obs if len(dig.left)==i]
'''
