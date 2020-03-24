# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# 1AC, DP solution
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        a = arr
        n = len(a)
        mx = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            mx[i][i] = a[i]
        for i in range(n):
            for j in range(i + 1, n):
                mx[i][j] = max(mx[i][j - 1], a[j])
        INT_MAX = 2 ** 31 - 1
        dp = [[INT_MAX for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for i in range(1, n):
            for j in range(n - i):
                for k in range(i):
                    dp[j][j + i] = min(dp[j][j + i], dp[j][j + k] + dp[j + k + 1][j + i]\
                        + mx[j][j + k] * mx[j + k + 1][j + i])
        return dp[0][n - 1]
