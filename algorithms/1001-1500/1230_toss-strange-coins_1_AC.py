# https://leetcode.com/problems/toss-strange-coins/
# 1AC, simple DP
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        p = prob
        n = len(p)
        t = target
        dp = [[0 for j in range(t + 1)] for i in range(n + 1)]

        dp[0][0] = 1.0
        for i in range(1, n + 1):
            dp[i][0] = (1 - p[i - 1]) * dp[i - 1][0]
            for j in range(1, min(t, i) + 1):
                dp[i][j] = p[i - 1] * dp[i - 1][j - 1]
                if i - 1 >= j:
                    dp[i][j] += (1 - p[i - 1]) * dp[i - 1][j]
        return dp[n][t]
