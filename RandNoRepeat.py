import random


def rand(num, val_1):
    numlst = []
    x = 0
    r = 0
    while len(numlst) < num:
        rnd = random.randint(val_1, num)
        if rnd in numlst:
            continue
        else:
            numlst += [rnd]
    for i in range(num):
        r = numlst[x]
        print(r)
        x += 1


rand(4, 1)
