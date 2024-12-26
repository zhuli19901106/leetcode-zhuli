# hard
# https://leetcode.com/problems/minimum-falling-path-sum-ii/
# strange, how is this hard?
# you got insane hard and easy hard at the same time, what you gonna do?
# forget about it
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        INT_MAX = (1 << 31) - 1

        g = grid
        n, m = len(g), len(g[0])

        dp = [[INT_MAX for j in range(m)] for i in range(n)]
        for j in range(m):
            dp[0][j] = g[0][j]
        for i in range(1, n):
            ml = [0 for j in range(m)]
            ml[0] = dp[i - 1][0]
            for j in range(1, m):
                ml[j] = min(ml[j - 1], dp[i - 1][j])

            mr = [0 for j in range(m)]
            mr[m - 1] = dp[i - 1][m - 1]
            for j in range(m - 2, -1, -1):
                mr[j] = min(mr[j + 1], dp[i - 1][j])

            for j in range(m):
                if j == 0:
                    dp[i][j] = mr[j + 1] + g[i][j]
                elif j == m - 1:
                    dp[i][j] = ml[j - 1] + g[i][j]
                else:
                    dp[i][j] = min(ml[j - 1], mr[j + 1]) + g[i][j]

        res = INT_MAX
        for j in range(m):
            res = min(res, dp[n - 1][j])
        return res
