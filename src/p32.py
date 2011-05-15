wanted = set(['1', '3', '2', '5', '4', '7', '6', '9', '8'])

def is9(i,j):
    si,sj,sk = str(i), str(j), str(i*j)
    ret = si + sj + sk
    return len(si + sj + sk)==9, set(ret)

products = []
for i in range(1,2000):
    for j in range(1, 2000):
        boo, got = is9(i,j)
        if boo and got==wanted:
            if i*j not in products:
                products.append(i*j)
                print i,j
        

print products, sum(products)

