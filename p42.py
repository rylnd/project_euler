def val(s):
    tot = 0
    for char in s:
        tot += ord(char)-64
    return tot

def tri(n):
    l = []
    for i in range(1,n+1):
        l.append(i*(i+1)/2)
    return l

tri = tri(1000)
words = open('words.txt').next().split(',')
words = map(lambda x: x.strip('"'), words)

final = [(word, val(word)) for word in words if val(word) in tri]
print final, len(final)

