class Solution(object):
    def singleNonDuplicate(self, n):
        li = len(n)-1
        lo = 0
        hi = li
        while lo <= hi:
            i = max(min((lo + hi) // 2, li), 0)
            if not i % 2:
                if i+1 <= li and n[i] == n[i+1]:
                    lo = min(i+2, li)
                elif i-1 >= 0 and n[i] == n[i-1]:
                    hi = max(i-2, 0)
                else:
                    return n[i]
            else:
                if i+1 <= li and n[i] == n[i+1]:
                    hi = max(i-1, 0)
                elif i-1 >= 0 and n[i] == n[i-1]:
                    lo = min(i+1, li)
                else:
                    return n[i]
        return n[lo]