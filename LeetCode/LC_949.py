import itertools as it

def largestTimeFromDigits(d):
    perms = it.permutations(d)
    best = None
    bestTime = -1
    for p in perms:
        if ((p[0] < 2) or (p[0] == 2 and p[1] < 4)) and p[2] < 6:
            time = p[0]*600 + p[1]*60 + p[2]*10 + p[3]
            if time > bestTime:
                bestTime = time
                best = p
    if best:
        return str(best[0]) + str(best[1]) + ':' + str(best[2]) + str(best[3])
    return ''