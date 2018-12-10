class Solution(object):
    def numDecodings(self, s):
        n = [int(x) for x in s]
        L = len(n)
        dp = [0] * L
        for i in range(L):
            if 1 <= n[i] <= 9:
                if i-1 >= 0:
                    dp[i] += dp[i-1]
                else:
                    dp[i] += 1
            if i > 0:
                if n[i-1] == 1 and 0 <= n[i] <= 9:
                    if i-2 >= 0:
                        dp[i] += dp[i-2]
                    else:
                        dp[i] += dp[i-1]
                elif n[i-1] == 2 and 0 <= n[i] <= 6:
                    if i-2 >= 0:
                        dp[i] += dp[i-2]
                    else:
                        dp[i] += dp[i-1]
        return dp[L-1]