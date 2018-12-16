class Solution(object):
    r = 0
    
    def reversePairs(self, n):
        self.merge(n)
        return self.r
        
    def merge(self, n):
        L = len(n)
        if L <= 1:
            return n
        half = L // 2
        left, right = self.merge(n[:half]), self.merge(n[half:])
        for r in right:
            inv = len(left) - bisect.bisect(left, 2*r)
            if inv:
                self.r += inv
            else:
                break
        return sorted(left+right)