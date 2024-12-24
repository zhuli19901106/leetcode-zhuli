# medium
# https://leetcode.com/problems/largest-plus-sign/
# 1AC, simple O(n^2) solution, how to achieve better complexity?
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        n = m = N
        a = [[1 for j in range(m)] for i in range(n)]
        for x, y in mines:
            a[x][y] = 0
        dp = [[[\
            0 for k in range(4)]\
            for j in range(m + 2)]\
            for i in range(n + 2)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1][j - 1] == 0:
                    continue
                dp[i][j][0] = dp[i - 1][j][0] + 1
                dp[i][j][1] = dp[i][j - 1][1] + 1
        for i in range(n, 0, -1):
            for j in range(m, 0, -1):
                if a[i - 1][j - 1] == 0:
                    continue
                dp[i][j][2] = dp[i + 1][j][2] + 1
                dp[i][j][3] = dp[i][j + 1][3] + 1
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, min(dp[i + 1][j + 1]))
        return res
