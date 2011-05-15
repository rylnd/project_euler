def prob10():
    sam = 2
    sm = 0
    for i in range(1, 1000):
        sam = sam * 2

    anstr = str(sam)
    for j in range(0, len(anstr)):
        sm += int(anstr[j])
    
    print sm

prob10()
