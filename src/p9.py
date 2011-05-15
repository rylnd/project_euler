'''yeah, this is brute force.  I'll try and think of something better 
later.  probably not though.'''
import os
def prob9():
    for a in range(1, 500):
        for b in range(1, 500):
            for c in range(1, 500):
                if ((a+b+c)==1000):
                    if((a*a + b*b)==c*c):
                        print 'a:%d b:%d c:%d prod: %d' % (a, b, c, a*b*c)
                        os._exit(0)
            




prob9()
