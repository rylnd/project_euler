#!/usr/bin/python
from __future__ import division
from operator import mul
def reduced(x,y):
    if x[0] in y:
        xnew = int(x.replace(x[0], ''))
        ynew = int(y.replace(x[0], ''))
        return int(x)/int(y)==xnew/ynew
    elif x[1] in y:
        xnew = int(x.replace(x[1], ''))
        ynew = int(y.replace(x[1], ''))
        return int(x)/int(y)==xnew/ynew

list = [str(i) for i in range(12,99) if str(i)[0]!=str(i)[1] if i%10!=0]

pairs = [(x,y) for x in list for y in list if x!=y if y>x]

wanted = [(int(x),int(y)) for x,y in pairs if reduced(x,y)]
print wanted
totx,toty = 1,1
for x,y in wanted:
    totx *= x
    toty *=y

print totx/toty
