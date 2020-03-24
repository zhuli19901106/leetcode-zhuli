# https://leetcode.com/problems/domino-and-tromino-tiling/
# linear DP solution
class Solution:
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.dp = [1]
        self.dps = [1]

    def numTilings(self, N: int) -> int:
        dp = self.dp
        dps = self.dps

        i = len(dp)
        while i <= N:
            res = 0
            res += dp[i - 1]
            if i >= 2:
                res += dp[i - 2]
            if i >= 3:
                res += 2 * dps[i - 3]
            res %= Solution.MOD
            dp.append(res)
            dps.append(res + dps[-1])
            i += 1
        return dp[N]
