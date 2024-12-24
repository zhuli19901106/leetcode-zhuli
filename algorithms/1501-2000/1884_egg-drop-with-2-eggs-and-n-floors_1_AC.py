# medium
# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/
# the DP relation isn't quite straight-forward after all
from math import sqrt

class Solution:
    def twoEggDrop(self, n: int) -> int:
        MAXVAL = (1 << 31) - 1
        k = 2
        dp = [[0 for j in range(n + 1)] for i in range(k)]

        for i in range(1, n + 1):
            dp[0][i] = i

        for ki in range(1, k):
            for i in range(1, n + 1):
                dp[ki][i] = MAXVAL
                ll = 1
                # almost cheating, except not really
                rr = min(i, 2 * int(sqrt(i)) + 1)
                for x in range(ll, rr + 1):
                    dp[ki][i] = min(dp[ki][i], max(dp[ki - 1][x - 1], dp[ki][i - x]) + 1)
        return dp[k - 1][n]
