# medium
# https://leetcode.com/problems/minimum-falling-path-sum/
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        a = A
        n = len(a)
        m = len(a[0])
        dp = [[0 for j in range(m)] for i in range(n)]
        for i in range(m):
            dp[0][i] = a[0][i]
        for i in range(1, n):
            for j in range(m):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])
                dp[i][j] += a[i][j]
        return min(dp[n - 1])
