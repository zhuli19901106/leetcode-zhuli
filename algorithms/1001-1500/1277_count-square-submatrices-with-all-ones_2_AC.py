# medium
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        a = matrix
        n = len(a)
        m = len(a[0])
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        res = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    continue
                dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + a[i][j]
                res += dp[i + 1][j + 1]
        return res
