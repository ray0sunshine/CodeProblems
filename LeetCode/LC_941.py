def validMountainArray(a):
    L = len(a)
    if L < 3:
        return False
    i = 0
    ascend = 0
    while i < L-1:
        diff = a[i+1] - a[i]
        if not diff:
            return False
        if ascend == 0:
            if diff < 0:
                return False
            ascend = 1
        elif ascend == 1:
            if diff < 0:
                ascend = 2
        else:
            if diff > 0:
                return False
        i += 1
    return ascend == 2