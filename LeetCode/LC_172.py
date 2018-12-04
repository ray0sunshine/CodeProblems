def trailingZeroes(n):
    fives = 0
    while n > 0:
        n //= 5
        fives += n
    return fives