from decimal import *

def spherePack(t, r):
    if len(r) < 2:
        return 2000 * r[0]

    # use diameter
    d = 2 * t

    # sort
    r.sort(reverse = True)

    # palindrome order select int 2 lists
    a = r[0:][::2]
    b = r[1:][::2]

    # calculate height minus final radius
    ah = Decimal(a[0]) + hSum(d, a)
    bh = Decimal(b[0]) + hSum(d, b)

    # merge heights using final elements d3 value only
    h = ah + bh + hSum(d, [a[-1], b[-1]])

    return round(Decimal(h * 1000))

def hSum(d, a):
    if len(a) < 2:
        return 0

    h = Decimal(0)
    for i in range(1, len(a)):
        rPair = a[i] + a[i-1]
        d1 = rPair * rPair
        cPair = d - rPair
        d2 = cPair * cPair
        h += Decimal(d1 - d2).sqrt()
    return h

t,n = (int(x) for x in input().split())
r = [int(x) for x in input().split()]
print(spherePack(t, r))

#print(spherePack(2, [2]))
#print(spherePack(5, [3, 4]))
#print(spherePack(100, [61, 62, 63, 64, 65]))