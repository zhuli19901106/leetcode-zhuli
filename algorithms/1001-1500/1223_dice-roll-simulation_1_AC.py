# hard
# https://leetcode.com/problems/dice-roll-simulation/
# 1AC, feeling a bit dizzy with such DP problems
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0 for k in range(16)] for j in range(6)] for i in range(n)]
        for i in range(6):
            dp[0][i][0] = dp[0][i][1] = 1
        rm = rollMax
        for i in range(1, n):
            for j in range(6):
                for k in range(6):
                    if j == k:
                        continue
                    dp[i][j][1] += dp[i - 1][k][0]
                for k in range(2, rm[j] + 1):
                    dp[i][j][k] = dp[i - 1][j][k - 1]
                for k in range(1, rm[j] + 1):
                    dp[i][j][0] += dp[i][j][k]
                for k in range(rm[j] + 1):
                    dp[i][j][k] %= MOD

        res = 0
        for i in range(6):
            res = (res + dp[n - 1][i][0]) % MOD
        return res
