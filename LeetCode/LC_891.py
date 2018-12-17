class Solution:
    def sumSubseqWidths(self, n):
        L = len(n) - 1
        return sum(v * ((1 << i) - (1 << (L - i))) for i,v in enumerate(sorted(n))) % 1000000007