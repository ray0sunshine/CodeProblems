import math

class Solution:
    def numFactoredBinaryTrees(self, a):
        a.sort()
        L = len(a)
        dp = dict(zip(a, [1]*L))
        for i in range(1, L):
            ai = a[i]
            airt = math.sqrt(ai)
            for j in range(i):
                aj = a[j]
                if aj > airt:
                    break
                if not ai % aj:
                    div = ai // aj
                    if div in dp:
                        dp[ai] += (1 if div == aj else 2) * dp[aj] * dp[div]
        return sum(dp.values()) % 1000000007