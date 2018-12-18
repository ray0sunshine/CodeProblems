class Solution:
    def minDeletionSize(self, a):
        L = len(a)
        w = len(a[0])
        dp = [1] * w
        for c in range(1, w):
            for d in range(c):
                if all(a[i][d] <= a[i][c] for i in range(L)):
                    dp[c] = max(dp[c], dp[d] + 1)
        return w - max(dp)