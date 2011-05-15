def digsum(x):
    return sum(int(digit) for digit in str(x))


l = [(a**b,digsum(a**b)) for a in range(1,101) for b in range(1,101)]

print len(l)

print max(l, key=lambda x: x[1])

        
    
