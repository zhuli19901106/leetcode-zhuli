# medium
# https://leetcode.com/problems/maximum-sum-of-an-hourglass/
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        g = grid
        n, m = len(g), len(g[0])
        sm = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n):
            for j in range(m):
                sm[i + 1][j + 1] = sm[i + 1][j] + sm[i][j + 1] - sm[i][j] + g[i][j]

        res = 0
        for i in range(2, n):
            for j in range(2, m):
                cur_sm = sm[i + 1][j + 1] + sm[i - 2][j - 2] - sm[i + 1][j - 2] - sm[i - 2][j + 1]
                cur_sm -= (g[i - 1][j - 2] + g[i - 1][j])
                res = max(res, cur_sm)

        return res
