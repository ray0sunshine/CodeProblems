class Solution(object):
    def jump(self, n):
        L = len(n) - 1
        if L < 1:
            return 0
        hi = n[0]
        j = 1
        i = 1
        while hi < L:
            j += 1
            lim = hi
            while i <= lim:
                hi = max(i + n[i], hi)
                i += 1
        return j