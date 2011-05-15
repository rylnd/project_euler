def prob20():
    tot = 0
    sum = 1
    for i in range(2, 100):
        sum = sum * i
    sum = str(sum)
    for j in range(0, len(sum)):
        tot += int(sum[j])

    print tot

prob20()
